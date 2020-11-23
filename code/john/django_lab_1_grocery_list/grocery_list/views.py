# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse

from django.utils import timezone
import datetime 

from .models import GroceryItem

def index(request):    
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    
    context = {
        'current_grocery_list': current_grocery_list,
        'completed_items': completed_items,
    }
    return render(request, 'grocery_list/index.html', context) # what to send to that URL


def add_item(request):    
    grocery_item = request.POST['item']  # post takes in name, not ID...
    print(f'Request is {request.POST}. add_item function running with grocery_item : {grocery_item}...')
    
    GroceryItem.objects.create(grocery_description=grocery_item) # .create() auto-saves it for you...
    
    return HttpResponseRedirect(reverse('grocery_list:index')) # TODO lookup wtf reverse does...  # reverse takes that and goes to empty


def update_or_delete(request):
    print('>>>>>PRINT: update_or_delete function running...')
    
    # Next step is to read documentation @ https://docs.djangoproject.com/en/3.1/topics/forms/#the-work-that-needs-to-be-done :


    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete_item(request):
    print('>>>>>PRINT: delete_item function running...')
    print(f'>>>>>PRINT: entire request.POST is {request.POST}.')
   
    # https://docs.djangoproject.com/en/3.1/ref/request-response/ :
    #     QueryDict.getlist(key, default=None)¶
    #     Returns a list of the data with the requested key. Returns an empty list if the key doesn’t exist and default is None. It’s guaranteed to return a list unless the default value provided isn’t a list.
    items_to_delete_list = request.POST.getlist('items_to_delete') # makes a list with QueryDict
    
    for item in items_to_delete_list:
        print(f'>>>>>PRINT: DELETING item is {item}.')
        GroceryItem.objects.filter(grocery_description=item).delete()

    print(f'>>>>>PRINT: All done.')

    return HttpResponseRedirect(reverse('grocery_list:index'))


def mark_completed(request):
    print('>>>>>PRINT: mark_completed function running...')
    
    update_list = request.POST.getlist('items_to_complete') # makes a list, see above: delete function comments and links
    
    # https://docs.djangoproject.com/en/3.1/topics/db/queries/

    for item in update_list:
        print(f'>>>>>PRINT: UPDATING item: {item}.')
        item = get_object_or_404(GroceryItem, grocery_description=item)
        print(item)
        
        item.completed = True
        item.completed_date=(timezone.now())
        item.save()

    print(f'>>>>>PRINT: All done.')

    return HttpResponseRedirect(reverse('grocery_list:index'))

def mark_incomplete(request):
    # do something!
    print('>>>>>PRINT: mark_incomplete function running...')
    print(f'>>>>>PRINT: entire request is {request}.')
    
    update_list = request.POST.getlist('mark_incomplete') # makes a list, see above: delete function comments and links
    
    for item in update_list:
        print(f'>>>>>PRINT: UPDATING item: {item}.')
        item = get_object_or_404(GroceryItem, grocery_description=item)
        print(f'>>>>>PRINT: UPDATING item: {item}.')
        
        item.completed = False
        item.save()

    print(f'>>>>>PRINT: All done.')

    return HttpResponseRedirect(reverse('grocery_list:index'))
