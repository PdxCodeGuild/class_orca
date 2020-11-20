from django.urls import path

from . import views

app_name = 'Posts'
urlpatterns = [
    path('', views.index, name='index')
]