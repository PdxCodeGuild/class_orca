
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='index'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='entry'),
    path('new/', views.BlogCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', views.BlogEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
]

    # path('', views.index, name='index'),

