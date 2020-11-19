from django.urls import path

from . import views 

app_name = 'ShortLink'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_code/', views.create_code, name='create_code'), 
    path('re_direct/<str:short_url>', views.re_direct, name='re_direct'),   
]