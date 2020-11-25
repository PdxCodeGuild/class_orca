from django.urls import path

from . import views

app_name = 'instaface'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
    # path('media/images/<str:post.photo.url>', views.LargeImageView.as_view(), name='largeimage'),

]
