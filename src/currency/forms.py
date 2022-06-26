from django import forms

from src.currency.models import Currency


class CreateCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ("name",)
