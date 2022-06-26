from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin

from src.user.user_manager import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True, verbose_name="Почта")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    is_admin = models.BooleanField(default=False, verbose_name="Админ")
    is_delete = models.BooleanField(default=False, blank=True, verbose_name="Удален")

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
