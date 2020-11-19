from django.urls import path
from . import views

app_name = 'url_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_url/', views.add_url, name='add_url'),
]