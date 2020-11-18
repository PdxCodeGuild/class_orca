from django.urls import path

from . import views

app_name = 'Urlapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
    path('results/', views.results, name='results')
]