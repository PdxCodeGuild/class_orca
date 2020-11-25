import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    tweet = models.CharField(max_length=180)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return self.tweet