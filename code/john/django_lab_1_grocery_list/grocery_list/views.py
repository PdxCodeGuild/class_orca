# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.

def index(request):    
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    
    print(current_grocery_list)
    # TODO I don't understand this:
    context = {
        'current_grocery_list': current_grocery_list,
        'completed_items': completed_items,
    }
    return render(request, 'grocery_list/index.html', context) # what to send to that URL

def add_item(request):
    # little confusing here
    grocery_item = request.POST['item']
    # print(grocery_item)
    GroceryItem.objects.create(grocery_description=grocery_item)
    # .create() auto-saves it for you...
    return HttpResponseRedirect(reverse('grocery_list:index'))