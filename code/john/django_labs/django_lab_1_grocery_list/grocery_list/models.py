# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

from django.db import models

from django.utils import timezone
import datetime 


class GroceryItem(models.Model):
    
    grocery_description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)

    created_date = models.DateTimeField(default=timezone.now())

    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.grocery_description