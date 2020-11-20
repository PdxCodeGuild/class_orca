from django.db import models
from django.utils import timezone

import datetime

class LongUrlShortCode(models.Model):
    long_url = models.CharField(max_length=200)
    short_code = models.CharField(max_length=6)

    def __str__(self):
            return self.long_url