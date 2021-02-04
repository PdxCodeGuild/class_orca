from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    item = models.CharField(max_length=100)
    added = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False)                                                              
    completed_date = models.DateTimeField(blank=True, null=True)

    # completed_check = False
    # if completed = True:
    #     completed_check = False

    # def publish(self):
    #     self.completed_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.item