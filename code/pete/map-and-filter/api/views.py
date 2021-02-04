from rest_framework import generics

from frontend.models import Programmer
from .serializers import ProgrammerSerializer

class ListProgrammer(generics.ListCreateAPIView):
  queryset = Programmer.objects.all()
  serializer_class = ProgrammerSerializer