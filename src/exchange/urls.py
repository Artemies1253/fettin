from django.urls import path

from src.exchange.views import CreateLotView

urlpatterns = [
    path("lot/create/", CreateLotView.as_view(), name="create_lot")
]
