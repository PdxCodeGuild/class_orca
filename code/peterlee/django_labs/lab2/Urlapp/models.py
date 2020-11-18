from django.db import models

class Bank(models.Model):
    new_code = models.CharField(max_length=200)
    original_url = models.CharField(max_length=400)

