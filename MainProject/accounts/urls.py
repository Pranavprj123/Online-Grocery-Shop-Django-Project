from django.contrib import admin
from django.urls import path,include
from accounts.views import *
from . import views



urlpatterns = [
    path('registration/', registration, name="registration"),
    path('login/', userlogin, name="userlogin"),
    path('profile/', profile, name="profile"),
    path('logout/', views.logoutuser, name="logout"),
    path('change-password/', change_password, name="change_password"),
    path('user-product/<int:pid>/', user_product, name="user_product"),
    path('product-detail/<int:pid>/', product_detail, name="product_detail"),
]