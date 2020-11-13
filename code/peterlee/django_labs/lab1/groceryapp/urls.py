from django.urls import path

from . import views

app_name = 'groceryapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('submitted/', views.submitted, name='submitted')
]