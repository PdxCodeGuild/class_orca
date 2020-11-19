from django.urls import path

from . import views

app_name = 'urlgen_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('<int:url_id>/re_direct/', views.re_direct, name='re_direct'),
]



    # path('add_item/', views.add_item, name='add_item'),
    # path('mark_complete/', views.mark_complete, name='mark_complete'),
    # path('delete_item/', views.delete_item, name='delete_item'),
    # path('returned/', views.returned, name='returned'),