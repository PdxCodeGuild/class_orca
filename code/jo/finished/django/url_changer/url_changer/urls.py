from django.urls import path

from . import views

app_name = 'url_changer'
urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
    path('redirect/<str:short_url>/', views.redirect, name='redirect'),
]
