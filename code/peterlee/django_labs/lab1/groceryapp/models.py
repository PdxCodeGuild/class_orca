from django.db import models
from django.utils import timezone

import datetime

class GroceryItem(models.Model):
    groceryitem_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    completion_date = models.DateTimeField('date completed', null=True, blank=True)
    completion_check = models.BooleanField(default=False)

    def __str__(self):
        return self.groceryitem_text