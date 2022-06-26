from django.db import models

from src.user.models import User
from src.currency.models import Currency


class Lot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lots", verbose_name="Пользователь")
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="lots", verbose_name="Вид продаваемой валюты"
    )
    selled_value = models.FloatField(verbose_name="Количество выставленной валюты")
    price = models.FloatField(verbose_name="Цена лота")
    price_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name="Вид ценовой валюты"
    )
    open = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
    )
    update_at = models.DateTimeField(
        "Дата изменения", auto_now=True
    )
