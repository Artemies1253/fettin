from django.db import models

from src.user.models import User
from src.currency.models import Currency


class TransactionExchange(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Покупатель", related_name="buyed_transactions", null=True
    )
    seller = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Покупатель",
        related_name="selled_transactions", null=True, blank=True, default=None
    )
    value_buyer = models.FloatField(
        verbose_name="Количество валюты которое потратил покупатель", null=True,
        blank=True, default=None
    )
    value_seller = models.FloatField(
        verbose_name="Количество валюты которое продал продавец", null=True, blank=True, default=None
    )
    currency_buyer = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, verbose_name="Тип валюты покупателя",
        related_name="buyed_transactions"
    )
    currency_seller = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, verbose_name="Тип валюты продавца",
        related_name="selled_transactions"
    )
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
    )


class TransactionReplenishment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="replenishment_transactions",
        verbose_name="Пользователь", null=True
    )
    value = models.FloatField(verbose_name="Сумма пополнения")
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, verbose_name="Вид пополняемой валюты",
        related_name="replenishment_transaction", null=True
    )
    created_at = models.DateTimeField(
        "Дата создания", auto_now_add=True
    )
