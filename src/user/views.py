from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import views
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from src.user.models import User


class LoginViews(LoginView):
    template_name = "users/login.html"


class LogoutViews(LogoutView):
    template_name = "users/logout.html"


class RegistrationView(views.View):
    def get(self, request):
        registration_form = RegistrationForm()
        return render(request, "users/registration.html",
                      {"registration_form": registration_form})

    def post(self, request):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            email = registration_form.cleaned_data["email"]
            raw_password = registration_form.cleaned_data["password_1"]
            user = User.objects.create_user(email=email, password=raw_password)
            user.first_name = registration_form.cleaned_data["first_name"]
            user.last_name = registration_form.cleaned_data["last_name"]
            user.save()
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, "users/registration.html",
                      {"registration_form": registration_form})


class UserInfoView(LoginRequiredMixin, generic.TemplateView):
    template_name = "users/info.html"
