from django.db import models

from src.user.models import User
from src.currency.models import Currency
from src.exchange.models import Lot


def create_lot(user: User, currency: Currency, value: float):
    lot = Lot.objects.create(user=user, currency=currency, value=value)