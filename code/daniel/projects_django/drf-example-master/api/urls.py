from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls 