from django.db import models
import datetime
from django.utils import timezone


class Grocerylist(models.Model):
    listitem = models.CharField(max_length=50)
    create_date = models.DateTimeField()
    completed_date = models.DateTimeField()
    completed_boolean = models.BooleanField(default = False)

    def __str__(self):
        return self.listitem