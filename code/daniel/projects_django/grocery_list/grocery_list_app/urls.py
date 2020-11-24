from django.urls import path

from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete_item/<int:item_id>', views.complete_item, name='complete_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('delete_complete/', views.delete_complete, name='delete_complete'),
]  

