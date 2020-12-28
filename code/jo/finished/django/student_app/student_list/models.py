from django.db import models

class Student_list(models.Model):
    name = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)
    favorite = models.CharField(max_length=200)

    def __str__(self):
        return self.name
