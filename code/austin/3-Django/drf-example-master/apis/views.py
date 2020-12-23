from django.shortcuts import render
from rest_framework import generics

from students import models
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = TodoSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

    