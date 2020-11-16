# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj
#  NOTE FOR THIS LAB, MERRITT WANTS FUNCTION-BASED VIEWS, NOT CLASS-BASED. BIT SIMPLER.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    print(f'Request is {request}. add_item function running...')
    
    grocery_item = request.POST['item']  # post takes in name, not ID...
    print(grocery_item)
    
    GroceryItem.objects.create(grocery_description=grocery_item) # .create() auto-saves it for you...
    
    # lookup wtf reverse does...  # reverse takes that and goes to empty
    return HttpResponseRedirect(reverse('grocery_list:index'))


# function A
# marking completed
def mark_completed(request):
    print(f'Request is {request}. Mark_Completed function running...')
    # Request is : <WSGIRequest: POST '/groceries/mark_completed/'>.

    # FOR loop????
    item = request.POST['']
    print(f'item is {item}. ...')

    print(f'item.completed is {item.completed}. ...')
    item.completed = True
    item.save()
    print(f'item.completed is {item.completed}. ...')

    # https://docs.djangoproject.com/en/3.1/topics/db/queries/
        # Be aware that the update() method is converted directly to an SQL statement. It is a bulk operation for direct updates. It doesn’t run any save() methods on your models, or emit the pre_save or post_save signals (which are a consequence of calling save()), or honor the auto_now field option. If you want to save every item in a QuerySet and make sure that the save() method is called on each instance, you don’t need any special function to handle that. Loop over them and call save():
        # for item in my_queryset:
        #     item.save()




    return HttpResponseRedirect(reverse('grocery_list:index'))


# function B
# one for deleting it from list...

def delete_item(request):
    #
    # https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects
    # 
    print(f'Request is {request}. delete_item function running...')

            # COPIED:
            # grocery_item = request.POST['item']            
            # GroceryItem.objects.create(grocery_description=grocery_item) # .create() auto-saves it for you...
            
    grocery_item = request.POST['item']
    print(f'item is {grocery_item}. ...')
    item.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))
