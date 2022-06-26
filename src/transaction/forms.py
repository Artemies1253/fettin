from django import forms

from src.transaction.models import TransactionReplenishment


class CreateTransactionReplenishmentForm(forms.ModelForm):
    class Meta:
        model = TransactionReplenishment
        exclude = ("created_at", "user")
