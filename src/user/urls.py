from django.urls import path
from .views import LoginViews, LogoutViews, RegistrationView, UserInfoView

urlpatterns = [
    path("login/", LoginViews.as_view(), name="login"),
    path("logout/", LogoutViews.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path('info/', UserInfoView.as_view(), name="user_info")
]
