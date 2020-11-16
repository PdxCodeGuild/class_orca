from django.db import models
from django.utils import timezone

import datetime

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def created_at(self):
        now = timezone.now()
        return now

    def completed_at(self):
        now = timezone.now()
        return now

    def __str__(self):
        return self.item_text
