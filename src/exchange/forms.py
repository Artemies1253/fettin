from django import forms
from django.core.exceptions import ValidationError

from src.exchange.models import Lot


class CreateLotForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = ("currency", "value")

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)