from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceyItem



def index(request):
    current_grocery_list = GroceyItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceyItem.objects.filter(completed=True).order_by('completed_date')
    context = {'current_grocery_list': current_grocery_list, 'completed_items': completed_items}
    return render(request, 'grocery_app/index.html', context)

def add_item(request):
    grocery_item = request.POST['item']
    GroceyItem.objects.create(item_text=grocery_item)
    return  HttpResponseRedirect(reverse('grocery_app:index'))

def complete_item(request, complete_id):
    grocery_item = get_object_or_404(GroceyItem, pk=complete_id)
    grocery_item.completed = True
    grocery_item.completed_date = timezone.now()
    grocery_item.save()
    return  HttpResponseRedirect(reverse('grocery_app:index'))

def delete_item(request, delete_id):
    grocery_item = get_object_or_404(GroceyItem, pk=delete_id)
    grocery_item.delete()
    return  HttpResponseRedirect(reverse('grocery_app:index'))




