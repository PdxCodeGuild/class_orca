# api_app urls.py file

from django.urls import path
from .views import StudentCreateView, StudentDetailView
# from .views import StudentViewSet

# from rest_framework.routers import DefaultRouter # ?? 
# router = DefaultRouter()
# router.register('students', StudentViewSet, basename='students')
# urlpatterns = router.urls 

urlpatterns = [
    path('students/<int:pk>', StudentDetailView.as_view()), # FIX
    path('students/', StudentCreateView.as_view()), # FIX
]