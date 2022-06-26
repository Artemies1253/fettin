from django.urls import path

from src.transaction.views import CreateTransactionReplenishmentView, TransactionExchangeView


urlpatterns = [
    path("create_replenishment/", CreateTransactionReplenishmentView.as_view(), name="create_replenishment"),
    path("create_exchange/<int:lot_id>", TransactionExchangeView.as_view(), name="create_exchange")
]
