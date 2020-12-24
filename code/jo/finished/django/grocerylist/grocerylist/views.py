from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

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

def edit(request):
    items = request.POST.getlist('i_id')
    if '_update' in request.POST:
        for item in items:
            checked_item = get_object_or_404(GroceryItem, pk = item)
            checked_item.completed = True
            checked_item.complete_date = timezone.now()
            checked_item.save()
    elif '_delete' in request.POST:
        for item in items:
            checked_item = get_object_or_404(GroceryItem, pk =item)
            checked_item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))

