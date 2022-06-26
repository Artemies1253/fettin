from django.urls import path

from src.currency.views import CreateCurrencyView, ListCurrencyView

urlpatterns = [
    path("create/", CreateCurrencyView.as_view(), name="create_currency"),
    path("list/", ListCurrencyView.as_view(), name="list_currency")
]
