from django.urls import path

from src.transaction.views import CreateTransactionReplenishmentView


urlpatterns = [
    path("create_replinishment/", CreateTransactionReplenishmentView.as_view(), name="create_replenishment")
]
