from django import forms
from django.utils.safestring import mark_safe


class ContactForm(forms.Form):
    stock_symbol = forms.CharField(label=mark_safe('Stock-Symbol'))
    timeline = forms.ChoiceField(choices=[('1m', '1 month'), ('3m', '3 months'), ('6m', '6 months'), ('1y', '1 year'), ('2y', '2 years'), ('5y', '5 years')],
                                 label=mark_safe('Time line'))
    parameter = forms.ChoiceField(choices=[('high', 'High'), ('low', 'Low'), ('open', 'Open'), ('close', 'Close')],
                                  label=mark_safe('Parameter Options'))
