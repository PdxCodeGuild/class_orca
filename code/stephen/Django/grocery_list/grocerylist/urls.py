from django.urls import path

from . import views

app_name = 'grocerylist'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_item/', views.add_item, name="add_item"),
    path('<int:pk>/delete_item/', views.delete_item, name="delete_item"),
    path('<int:pk>/completed/', views.completed, name="completed"),
    path('<int:pk>/readd/', views.readd, name="readd"),
]