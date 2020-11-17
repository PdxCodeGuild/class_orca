from django.db import models
import datetime
from django.utils import timezone


class Grocerylist(models.Model):
    item_text = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(blank=True, null=True)
    completed_boolean = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text