from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Grocerylist

def index(request):
    current_grocery_list = Grocerylist.objects.filter(completed_boolean=False).order_by('create_date')
    completed_items = Grocerylist.objects.filter(completed_boolean=True)
    context = {
        'current_grocery_list': current_grocery_list,
        'completed_items': completed_items
        }
    return render(request, 'grocerylist/index.html', context)

def add_item(request):
    grocery_item = request.POST['item']
    Grocerylist.objects.create(item_text=grocery_item)
    return HttpResponseRedirect(reverse('grocerylist:index'))

