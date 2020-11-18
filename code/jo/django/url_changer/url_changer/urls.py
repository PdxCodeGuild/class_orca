from django.urls import path

from . import views

app_name = 'url_changer'
urlpatterns = [
    path('', views.index, name='index'),
    # path('add_item/', views.add_item, name='add_item'),
    # path('edit', views.edit, name="edit"),
    path('convert/', views.convert, name='convert'),
    path('redirect/', views.redirect, name='redirect'),
    
]
