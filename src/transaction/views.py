from django import views
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.forms import Form

from src.currency.models import CurrencyUser
from src.exchange.models import Lot
from src.transaction.forms import CreateTransactionReplenishmentForm
from src.transaction.services import create_replenishment_transaction, create_exchange_transaction


class CreateTransactionReplenishmentView(views.View):

    def get(self, request):
        form = CreateTransactionReplenishmentForm()
        return render(request, "transaction/create_transaction_replenishment.html",
                      {"form": form})

    def post(self, request):
        form = CreateTransactionReplenishmentForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get("value")
            currency = form.cleaned_data.get("currency")
            create_replenishment_transaction(user=request.user, currency=currency, count=value)
            return HttpResponseRedirect("/user/info")
        return render(request, "transaction/create_transaction_replenishment.html",
                      {"form": form})


class TransactionExchangeView(views.View):
    def post(self, request, lot_id):
        print()

        lot = Lot.objects.get(id=lot_id)
        seller = lot.user
        buyer = request.user
        value_seller = lot.selled_value
        value_buyer = lot.price
        kind_currency_buyer = lot.price_currency
        kind_currency_seller = lot.currency

        buyer_currency = CurrencyUser.objects.get(user=buyer, currency=kind_currency_buyer)
        seller_currency = CurrencyUser.objects.get(user=seller, currency=kind_currency_seller)
        if value_buyer <= buyer_currency.count:
            print("Не достаточно денег у покупателя")
            pass
        elif value_seller <= seller_currency.count:
            print("Не доастаточно денег у продавца")
            pass

        transaction = create_exchange_transaction(
            buyer=buyer, seller=seller,
            value_buyer=value_buyer, value_seller=value_seller,
            kind_currency_buyer=kind_currency_buyer, kind_currency_seller=kind_currency_seller
        )

        lot.open = False
        lot.save()

        return HttpResponseRedirect("/user/info")
