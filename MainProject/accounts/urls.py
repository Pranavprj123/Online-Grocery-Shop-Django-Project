from django.contrib import admin
from django.urls import path,include
from accounts.views import *
from . import views



urlpatterns = [
    path('registration/', registration, name="registration"),
    path('login/', userlogin, name="userlogin"),
    path('profile/', profile, name="profile"),
    path('logout/', views.logoutuser, name="logout"),
]