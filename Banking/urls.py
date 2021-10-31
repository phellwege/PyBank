from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration',views.regis),
    path('login',views.login),
    path('login_page',views.login_page),
    path('register_page',views.register),
    path('logout',views.logout),
]
