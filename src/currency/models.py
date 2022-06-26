from django.db import models

from src.user.models import User


class Currency(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя валюты", unique=True)

    # def __str__(self):
    #     return f"{self.name}"


class CurrencyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="currencies", verbose_name="Пользователь")
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name="Вид валюты", related_name="currency_users"
    )
    count = models.FloatField(verbose_name="Количество валюты")

    # def __str__(self):
    #     return f"Пользователь {self.user} имеет {self.count} {self.currency}"
