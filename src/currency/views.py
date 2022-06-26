from django.shortcuts import render
from django.views import generic

from src.currency.forms import CreateCurrencyForm
from src.currency.models import  Currency


class CreateCurrencyView(generic.CreateView):
    form_class = CreateCurrencyForm
    template_name = "currency/create_currency.html"
    success_url = "/"


class ListCurrencyView(generic.ListView):
    queryset = Currency.objects.all()
    template_name = "currency/currency_list.html"
    context_object_name = "currency_list"
