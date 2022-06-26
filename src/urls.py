from django.urls import path, include

from src.views import MainView

urlpatterns = [
    path('user/', include("src.user.urls")),
    path("currency/", include("src.currency.urls")),
    path("transaction/", include("src.transaction.urls")),
    path("exchange/", include("src.exchange.urls")),
    path('', MainView.as_view(), name='home')
]
