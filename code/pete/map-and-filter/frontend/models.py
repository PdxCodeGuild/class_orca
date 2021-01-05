from django.db import models

class Programmer(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  github_username = models.CharField(max_length=50, blank=True)
