from django.contrib import admin
from django.urls import path,include
from accounts.views import *



urlpatterns = [
    path('registration/', registration, name="registration"),
    path('login/', userlogin, name="userlogin"),
]