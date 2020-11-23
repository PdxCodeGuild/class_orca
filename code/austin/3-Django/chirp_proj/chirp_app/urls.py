from django.urls import path 
from . import views

app_name = 'chirp_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/', views.blog, name = 'blog'),
    path('post/', views.post, name = 'post'),
]
