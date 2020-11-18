from django.urls import path

from . import views


app_name = "url_shortner_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('url_source/', views.url_source, name='url_source'),
    path('user_redirect/<str:url_code>/', views.user_redirect, name='user_redirect'),
]
