from django.db import models
from django.utils import timezone

import datetime

class URL(models.Model):
    url_text = models.CharField(max_length=200)
    short_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    code_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.short_code
    
    def __str__(self):
        return self.url_text