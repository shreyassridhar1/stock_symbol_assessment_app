# import requests
# from django.shortcuts import render
from io import StringIO, BytesIO
import requests
import json
import matplotlib.pyplot as plt
import base64

from django.http import HttpResponse, response

from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg
from rest_framework import status

from .forms import ContactForm


def list(request):
    graphic = None
    res = []

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            stock_symbol = form.cleaned_data['stock_symbol']
            parameter = form.cleaned_data['parameter']
            timeline = form.cleaned_data['timeline']

            url = requests.get('https://api.iextrading.com/1.0/stock/{}/chart/{}'.format(stock_symbol, timeline), verify=False)  # Consuming API

            if url.status_code == 404:
                return HttpResponse('Unknown Stock Symbol', status.HTTP_400_BAD_REQUEST)  # Applied Check to see if stock is valid or not

            content = url.content
            string_content = content.decode("utf-8")
            jdata = json.loads(string_content)
            for obj in jdata:
                param_obj = obj.get('{}'.format(parameter))
                res.append(param_obj)


            fig, ax = plt.subplots()
            ax.plot(res)
            ax.set(xlabel='Timeline({}) ------->'.format(timeline), ylabel='Parameter ({}) ------>'.format(parameter),
                   title='Graphical representation of stock symbol --> ({}) '.format(stock_symbol))
            ax.grid()


            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graphic = base64.b64encode(image_png)
            graphic = graphic.decode('utf-8')


    form = ContactForm()

    return render(request, 'form.html', {'form': form, 'content': graphic})