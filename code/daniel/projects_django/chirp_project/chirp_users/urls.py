from django.urls import path

from . import views 

app_name = 'chirp_users'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfile.as_view(), name='profile'),
] 