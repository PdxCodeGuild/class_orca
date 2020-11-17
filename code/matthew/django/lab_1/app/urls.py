from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/mark_complete/', views.mark_complete, name='mark_complete')
]