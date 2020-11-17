from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    complete_grocery_list = GroceryItem.objects.all().filter(completion_check=True)
    incomplete_grocery_list = GroceryItem.objects.all().filter(completion_check=False)
    context = {'complete_grocery_list': complete_grocery_list, 'incomplete_grocery_list': incomplete_grocery_list}
    return render(request, 'groceryapp/index.html', context)

def add(request):
    new_entry = GroceryItem(groceryitem_text=request.POST.get('entry'), pub_date=timezone.now())
    new_entry.save()
    return HttpResponseRedirect(reverse('groceryapp:index'))

def complete(request, pk):
    entry = GroceryItem.objects.get(pk=pk)
    entry.completion_check = True
    entry.completion_date = timezone.now()
    entry.save()
    return HttpResponseRedirect(reverse('groceryapp:index'))

def incomplete(request, pk):
    entry = GroceryItem.objects.get(pk=pk)
    entry.completion_check = False
    entry.completion_date = None
    entry.save()
    return HttpResponseRedirect(reverse('groceryapp:index'))

def delete(request, pk):
    entry = GroceryItem.objects.get(pk=pk)
    entry.delete()
    return HttpResponseRedirect(reverse('groceryapp:index'))



