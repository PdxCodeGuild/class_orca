from django.db import models

class Shortener(models.Model):
    short_url = models.CharField(max_length=6, blank=True, null=True)
    long_url = models.CharField(max_length=200, blank=False, null=True)


    def __str__(self):
        return self.long_url
