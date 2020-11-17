from django.urls import path
from . import views

app_name = 'grocery_list_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('mark_complete/<int:item_id>', views.mark_complete, name='mark_complete'),
]