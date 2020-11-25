
from django.db import models
from django.utils import timezone

import datetime
 
class Items(models.Model):
    item_text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(null=True, blank=True)

    def was_created_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.created_date <= now

    def __str__(self):
        return self.item_text
        # returns string instead of object type
