from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserLoginView, RegisterView

#url path /api/user/*

urlpatterns = [
    path('login', UserLoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
]

urlpatterns = format_suffix_patterns(urlpatterns)