from django.urls import path

from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit', views.edit, name="edit"),
]
