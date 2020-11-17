from django.db import models

class Bank(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=400)

