from rest_framework import serializers
from frontend.models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Programmer
    fields = '__all__'