from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name="login"),
    path('login_key/', views.login_key, name="login_key"),
    path('register/', views.register_page, name="register"),
    path('register_key/', views.register_key, name="register_key"),
    path('logout_key/', views.logout_key, name="logout_key"),
    path('submit_key/', views.submit_key, name="submit_key"),
    path('<int:pk>/update/', views.update_page, name="update_page"),
    path('<int:pk>/update_key/', views.update_key, name="update_key"),
    path('<int:pk>/delete_key/', views.delete_key, name="delete_key"),
]

