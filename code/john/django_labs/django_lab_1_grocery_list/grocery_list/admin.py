# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

from django.contrib import admin

# Register your models here.
from .models import GroceryItem

admin.site.register(GroceryItem)