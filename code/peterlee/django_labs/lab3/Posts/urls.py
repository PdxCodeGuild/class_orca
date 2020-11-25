from django.urls import path

from . import views

app_name = 'Posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>', views.detail, name='detail'),
    path('create/', views.PostsCreateView.as_view(), name='create'),
    path('edit/<int:pk>', views.PostsEditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]