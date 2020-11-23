from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'app_lab_2' 

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('<str:code>/', views.redirect_def, name='redirect')
]
