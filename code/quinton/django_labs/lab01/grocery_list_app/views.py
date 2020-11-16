from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    context = {
        'current_grocery_list': current_grocery_list,
        'completed_items': completed_items
        }
    return render(request, 'grocery_list_app/index.html', context)

def add_item(request):
    grocery_item = request.POST['item']
    GroceryItem.objects.create(text_description=grocery_item)
    return HttpResponseRedirect(reverse('grocery_list_app:index'))

def mark_complete():
    pass

def delete_item():
    pass
  
