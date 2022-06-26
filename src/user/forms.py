from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from src.user.models import User


class RegistrationForm(forms.ModelForm):
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get("password_1")
        password_2 = cleaned_data.get("password_2")

        if password_1 != password_2:
            raise ValidationError("Пароли не совпадают")

    class Meta:
        model = User
        fields = ["email", "password_1", "password_2",
                  "first_name", "last_name"]
