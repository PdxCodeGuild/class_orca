# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

from django.shortcuts import render
from django.http import HttpResponse

from .models import GroceryItem

#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.

def index(request):
    
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by_('created_date')
    print(current_grocery_list)
    # TODO I don't understand this:
    context = {'current_grocery_list': current_grocery_list}

    return render(request, 'grocery_list/index.html', context) # what to send to that URL