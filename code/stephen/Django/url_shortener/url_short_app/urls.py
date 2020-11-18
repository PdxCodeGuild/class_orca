from django.urls import path

from . import views

app_name = 'url_short_app'

urlpatterns= [
    path('', views.index, name="index"),
    path('convert_url/', views.convert_url, name='conveert_url'),
    path('submit_long/', views.submit_long, name='submit_long'),
    path('<str:token>', views.redirect_url, name='redirect'),

]
