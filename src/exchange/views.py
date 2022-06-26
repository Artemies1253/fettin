from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import views

from src.exchange.forms import CreateLotForm
from src.exchange.models import Lot
from src.exchange.services import create_lot
from src.currency.models import CurrencyUser


class CreateLotView(views.View):
    def get(self, request):
        form = CreateLotForm()
        return render(request, "transaction/create_transaction_replenishment.html",
                      {"form": form})

    def post(self, request):
        form = CreateLotForm(data=request.POST)

        if form.is_valid():
            user = request.user
            selled_value = form.cleaned_data.get("selled_value")
            currency = form.cleaned_data.get("currency")
            price = form.cleaned_data.get("price")
            price_currency = form.cleaned_data.get("price_currency")
            user_currency = CurrencyUser.objects.filter(currency=currency, user=user)
            if not user_currency.exists():
                form.add_error("value", "Не достаточно средств")
                return render(request, "transaction/create_transaction_replenishment.html",
                              {"form": form})
            if user_currency.first().count < selled_value:
                form.add_error("value", "Не достаточно средств")
                return render(request, "transaction/create_transaction_replenishment.html",
                          {"form": form})
            create_lot(
                user=user, currency=currency, selled_value=selled_value, price=price, price_currency=price_currency
            )
            return HttpResponseRedirect("/")
        return render(request, "transaction/create_transaction_replenishment.html",
                      {"form": form})


class ListLotView(views.generic.ListView):
    queryset = Lot.objects.filter(open=True)
    context_object_name = "lot_list"
    template_name = "exchange/lot_list.html"

