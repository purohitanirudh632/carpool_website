
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('auth/user/login', user_login),
    path('auth/user/register', user_register),
    path('auth/driver/login', driver_login),
    path('auth/driver/register', driver_register),

    path('user_view', user_view),
    path('driver_view', driver_view),


]
