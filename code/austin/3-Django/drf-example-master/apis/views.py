from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse

from students import models
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
 
class CreateStudent(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer