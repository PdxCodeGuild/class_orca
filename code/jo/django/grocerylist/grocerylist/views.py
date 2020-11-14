from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import GroceryItem

def index(request):
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('added')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    context = {'current_grocery_list': current_grocery_list, 'completed_items': completed_items}
    return render(request, 'grocerylist/index.html', context)

def add_item(request):
    grocery_item = request.POST['item']
    GroceryItem.objects.create(item= grocery_item)
    return HttpResponseRedirect(reverse('grocerylist:index'))