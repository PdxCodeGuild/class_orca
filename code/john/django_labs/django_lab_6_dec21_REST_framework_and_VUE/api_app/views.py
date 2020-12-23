# THIS FILE IS THE ApiAppConfig api_app views.py

from rest_framework import generics, viewsets # viewset = set of generic views
# from django.something.... import User

from students.models import Student
from .serializers import StudentSerializer
# from .permissions import ReadOnly

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # another way
    # permission_classes = (ReadOnly)


# # see merritt's example for how to do more permissions
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all() # Users???
#     serializer_class = StudentSerializer


# these two are the old ones from before combining into one ViewSet
class StudentCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
