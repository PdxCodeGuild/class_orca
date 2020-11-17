from django.urls import path

from . import views

app_name = 'url_short_app'

urlpatterns= [
    path('', views.testfunction, name="index"),

]
