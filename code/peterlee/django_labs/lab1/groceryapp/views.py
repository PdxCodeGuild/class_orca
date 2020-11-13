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

def submit(request):
    if request.method == 'POST':
        new_entry = GroceryItem(groceryitem_text=request.POST.get('entry'), pub_date=timezone.now())
        new_entry.save()

        return HttpResponseRedirect(reverse('groceryapp:submitted'))

def submitted(request):
    return render(request, 'groceryapp/submitted.html')