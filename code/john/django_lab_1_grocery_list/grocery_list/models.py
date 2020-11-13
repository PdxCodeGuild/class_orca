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

        # what goes here?
        # https://docs.djangoproject.com/en/3.1/ref/models/fields/#booleanfield :
        # BooleanField
        # class BooleanField(**options)
        # A true/false field.
        # The default form widget for this field is CheckboxInput, or NullBooleanSelect if null=True.
        # The default value of BooleanField is None when Field.default isn’t defined.

    # TODO IS THE BELOW CORRECT, NECESSARY, GOOD IDEA?
    def __str__(self):
        return self.grocery_description


    # REQUIREMENTS FROM LAB DESC:
    #... with a model called GroceryItem which contains
    # 	1.  a text description, 
    # 	2. a created date, 
    # 	3. a completed date, 
    # 	4. and a boolean representing whether it was completed.
