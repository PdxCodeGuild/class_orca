from django.urls import path
from . import views

app_name = 'grocery_list_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
]