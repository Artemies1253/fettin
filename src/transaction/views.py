from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render

from src.transaction.forms import CreateTransactionReplenishmentForm
from src.transaction.services import create_replenishment_transaction


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
