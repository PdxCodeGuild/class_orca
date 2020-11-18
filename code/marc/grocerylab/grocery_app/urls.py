from django.urls import path

from . import views 

app_name = 'grocery_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete_item/<int:complete_id>', views.complete_item, name='complete_item'),
    path('delete_item/<int:delete_id>', views.delete_item, name='delete_item'),
]
