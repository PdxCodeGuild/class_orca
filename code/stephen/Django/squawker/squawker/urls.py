from django.urls import path

from . import views

app_name = 'squawker'

urlpatterns = [
    path('', views.SqueekListView.as_view(), name = 'home'),
    path('squawker/new/', views.SqueekCreateView.as_view(), name = 'new'),
    path('squawker/<int:pk>/', views.SqueekDetailView.as_view(), name = 'detail'),
    path('squawker/<int:pk>/edit/', views.SqueekEditView.as_view(), name='edit'),
    path('squawker/<int:pk>/delete/', views.SqueekDeleteView.as_view(), name='delete'),
    
] 