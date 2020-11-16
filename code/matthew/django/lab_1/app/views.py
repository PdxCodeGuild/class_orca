from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import GroceryItem


def index(request):
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    print(current_grocery_list)
    print(completed_items)
    context = {'current_grocery_list': current_grocery_list, 'completed_items': completed_items}
    return render(request, 'app/index.html', context)


def add_item(request):
    grocery_item = request.POST['item']
    GroceryItem.objects.create(item_text=grocery_item)
    return HttpResponseRedirect(reverse('app:index'))

def delete(request, pk):
    del_item = get_object_or_404(GroceryItem, pk=pk)
    del_item.delete()
    return HttpResponseRedirect(reverse('app:index'))

def mark_complete(request, pk):
    select_complete = get_object_or_404(GroceryItem, pk=pk)
    # print(select_complete)
    # print(select_complete.completed)
    select_complete.completed = True
    completed_date
    # print(select_complete.completed)
    select_complete.save()
    return HttpResponseRedirect(reverse('app:index'))
