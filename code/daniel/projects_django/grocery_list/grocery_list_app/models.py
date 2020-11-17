from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):

    grocery_item = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now())
    date_complete = models.DateTimeField(null=True, blank=True)
    item_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.grocery_item