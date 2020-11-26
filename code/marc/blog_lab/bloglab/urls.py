from django.urls import path

from . import views

app_name = 'bloglab'

urlpatterns = [
    path('', views.RagePageListView.as_view(), name='home'),
    path('ragepage/<int:pk>/', views.RagePageDetailView.as_view(), name='detail'),
    path('ragepage/new/', views.RagePageCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.RagePageEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.RagePageDeleteView.as_view(), name='delete'),
    
]