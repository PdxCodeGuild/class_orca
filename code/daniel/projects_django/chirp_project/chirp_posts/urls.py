from django.urls import path

from . import views 

app_name = 'chirp_posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('likes/', views.likes, name="likes"),
    path('post/new/', views.NewPostView.as_view(), name='new'), 
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'), 
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
] 