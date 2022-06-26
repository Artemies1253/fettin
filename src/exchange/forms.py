from django import forms
from django.core.exceptions import ValidationError

from src.exchange.models import Lot


class CreateLotForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = ("currency", "selled_value", "price", "price_currency")
