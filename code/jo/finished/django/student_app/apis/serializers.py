from rest_framework import serializers
from student_list import models


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'hometown',
            'favorite',
        )
        model = models.Student_list