from django.db import models
from django.utils import timezone

class GroceyItem(models.Model):

    item_text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(null=True, blank=True)

    
    def __str__(self):
        return self.item_text
    