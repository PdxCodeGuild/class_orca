from django.urls import path
from . import views

app_name = 'urls_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten, name='shorten'),
    path('<str:short_code>', views.goto, name='goto'),
]