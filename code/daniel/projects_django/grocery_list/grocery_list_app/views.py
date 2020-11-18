from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse 
from django.utils import timezone 

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.filter(item_complete=False).order_by('date_created')
    completed_list = GroceryItem.objects.filter(item_complete=True).order_by('date_complete')
    context = {'grocery_list': grocery_list, 'completed_list': completed_list} 
    return render(request, 'grocery_list_app/index.html', context)

def add_item(request):
    new_item = request.POST['grocery_item']
    print(request.POST)
    GroceryItem.objects.create(grocery_item=new_item)
    return HttpResponseRedirect(reverse('grocery_list_app:index'))

def complete_item(request, item_id):
    completed_item = get_object_or_404(GroceryItem, pk=item_id)
    completed_item.item_complete = True
    completed_item.date_complete = timezone.now() 
    completed_item.save() 
    return HttpResponseRedirect(reverse('grocery_list_app:index'))

def delete_item(request, item_id):
    deleted_item = get_object_or_404(GroceryItem, pk=item_id)
    deleted_item.delete() 
    return HttpResponseRedirect(reverse('grocery_list_app:index'))

def delete_complete(request):
    deleted_items = GroceryItem.objects.filter(item_complete=True)
    deleted_items.delete()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))
    