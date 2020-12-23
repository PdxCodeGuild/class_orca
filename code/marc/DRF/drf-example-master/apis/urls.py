#apis/urls.py
from django.urls import path

# from .views import ListStudent, DetailStudent

from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls

# urlpatterns = [
#     path('', ListStudent.as_view()),
#     path('<int:pk>/', DetailStudent.as_view()),
# ]