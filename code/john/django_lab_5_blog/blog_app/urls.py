
from django.urls import path

from . import views

# this urls.py is in the app folder
app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('blog_app/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('blog_app/new/', views.BlogCreateView.as_view(), name='new_post'),
    path('blog_app/<int:pk>/edit/', views.BlogEditView.as_view(), name='edit_post'),
    path('blog_app/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_post'),
]