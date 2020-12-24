from django.urls import path

from .views import ListStudents, DetailStudents

urlpatterns = [
    path('', ListStudents.as_view()),
    path('<int:pk>/', DetailStudents.as_view()),
]
