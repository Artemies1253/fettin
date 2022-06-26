from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import views

from src.exchange.forms import CreateLotForm


class CreateLotView(views.View):
    def get(self, request):
        form = CreateLotForm()
        return render(request, "transaction/create_transaction_replenishment.html",
                      {"form": form})

    def post(self, request):
        data = request.Post
        data["user"] = request.user
        form = CreateLotForm(data=data)

        if form.is_valid():
            return HttpResponseRedirect("/")
