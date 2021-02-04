from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'url_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('redirect/<str:short_code>/', views.redirect, name='redirect'),
]
