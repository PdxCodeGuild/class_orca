from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import GroceryItem

def index(request):
    grocery_list = GroceryItem.objects.filter(is_completed=False).order_by('date_created')
    done_list = GroceryItem.objects.filter(is_completed=True).order_by('date_created')
    context = {'grocery_list': grocery_list, 'done_list': done_list}
    return render(request, 'grocery/index.html', context)

def create(request):
    new_item = request.POST["item"]
    GroceryItem.objects.create(item_text=new_item, date_created=timezone.now())
    return HttpResponseRedirect(reverse('grocery_app:index'))

def delete(request, pk):
    del_item = get_object_or_404(GroceryItem, pk=pk)
    del_item.delete()
    return HttpResponseRedirect(reverse('grocery_app:index'))

def update(request, pk):
    update_item = get_object_or_404(GroceryItem, pk=pk)
    update_item.is_completed = True
    update_item.date_completed = timezone.now()
    update_item.save()
    return HttpResponseRedirect(reverse('grocery_app:index'))
