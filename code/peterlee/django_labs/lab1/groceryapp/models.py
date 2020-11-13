from django.db import models

class GroceryItem(models.Model):
    groceryitem_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    completion_date = models.DateTimeField('date completed')
    completion_check
