from django.urls import path

from .views import StudentList, StudentDetail

urlpatterns = [
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('students/', StudentList.as_view())
]