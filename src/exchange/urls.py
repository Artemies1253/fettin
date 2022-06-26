from django.urls import path

from src.exchange.views import CreateLotView, ListLotView

urlpatterns = [
    path("lot/create/", CreateLotView.as_view(), name="create_lot"),
    path("lot/list", ListLotView.as_view(), name="lot_list")
]
