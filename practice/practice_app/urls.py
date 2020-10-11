from django.contrib import admin
from django.urls import path,include
from practice_app import views

urlpatterns = [
    path('home',views.landing_page ,name = 'home_page'),
]
