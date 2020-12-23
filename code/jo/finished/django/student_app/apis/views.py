from django.shortcuts import render

from rest_framework import generics

from student_list import models
from .serializers import ListSerializer

class ListStudents(generics.ListCreateAPIView):
    queryset = models.Student_list.objects.all()
    serializer_class = ListSerializer

class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student_list.objects.all()
    serializer_class = ListSerializer