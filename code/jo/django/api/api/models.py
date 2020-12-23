from django.db import models

class Api(models.Model):
    student_name = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name
