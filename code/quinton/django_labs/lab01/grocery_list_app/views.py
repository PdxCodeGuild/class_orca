from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem


def index(request):
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    context = {
        'current_grocery_list': current_grocery_list,
        'completed_items': completed_items,
        }
    return render(request, 'grocery_list_app/index.html', context)

def add_item(request):
    grocery_item = request.POST['item']
    GroceryItem.objects.create(text_description=grocery_item)
    return HttpResponseRedirect(reverse('grocery_list_app:index'))

def mark_complete(request, item_id):
    mark_complete = get_object_or_404(GroceryItem, pk=item_id)
    mark_complete.completed = True
    mark_complete.completed_date = timezone.now()
    mark_complete.save()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))


def delete_item(request, item_id):
    delete_item = get_object_or_404(GroceryItem, pk=item_id)
    delete_item.delete()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))


  
