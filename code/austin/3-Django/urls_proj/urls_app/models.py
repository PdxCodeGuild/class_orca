from django.db import models
from django.utils import timezone

import datetime

class URL(models.Model):
    url_text = models.CharField(max_length=200)
    short_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    code_assigned = models.BooleanField(default=False)
    clicks = models.IntegerField(default=0)
    ip = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    dinner = models.CharField(max_length=200, null=True, blank=True)
    social = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code, self.url_text