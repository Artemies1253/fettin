from django.db import models

from src.user.models import User
from src.currency.models import Currency, CurrencyUser
from src.exchange.models import Lot


def create_lot(
        user: User, currency: Currency, price_currency: Currency, selled_value: float, price: float
):
    Lot.objects.create(
        user=user, currency=currency, selled_value=selled_value, price=price, price_currency=price_currency
    )
