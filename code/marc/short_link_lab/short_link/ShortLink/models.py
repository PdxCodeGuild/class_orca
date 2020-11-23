from django.db import models
from django.utils import timezone

class ShortLink(models.Model):

    url_link = models.TextField()
    short_url = models.CharField(max_length= 5)
    

    
    def __str__(self):
        return self.short_url