from rest_framework import generics
from rest_framework import viewsets

from students import models
from .serializers import StudentSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

# class ListStudent(generics.ListCreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer


# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer
