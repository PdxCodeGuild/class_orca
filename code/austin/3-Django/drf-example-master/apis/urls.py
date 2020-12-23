from django.urls import path

from .views import ListStudent, DetailStudent, CreateStudent

app_name = 'apis'
urlpatterns = [
    path('', ListStudent.as_view()),
    path('', CreateStudent.as_view()),
    path('<int:pk>/', DetailStudent.as_view()),
]
