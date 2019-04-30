from django.conf.urls import url
# from django.urls import path
from . import views
# from stock_symbols.views import StockSymbolViewSet

urlpatterns = [
    # path('stock_symbols/urls/appointment', StockSymbolViewSet.as_view({'get': 'list'}), name='stocksymbol-list'),
    url(r'list/', views.list)
]