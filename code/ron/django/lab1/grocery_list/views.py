# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Items

def index(request):
    completed_items = Items.objects.filter(completed=True).order_by('completed_date')
    current_grocery_list = Items.objects.filter(completed=False).order_by('created_date')
    context = {'current_grocery_list': current_grocery_list, 'completed_items': completed_items}
    return render(request, 'grocery_list/index.html', context)

def add_item(request):
    new_grocery_item = request.POST['item']
    Items.objects.create(item_text=new_grocery_item) # .create allows it to be written AND saved to the .db vs. .add and .save
    return HttpResponseRedirect(reverse('grocery_list:index'))

def mark_complete(request):
    select_complete = request.POST['complete']
    print(select_complete)
    print (request.POST)
    comp_item = Items.objects.get(pk = select_complete)
    comp_item.completed = True
    comp_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request):
    del_item = request.POST['delete']
    print(del_item)
    del_item1 = Items.objects.get(pk = del_item)
    del_item1.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def returned(request):
    select_complete = request.POST['complete']
    print(select_complete)
    print (request.POST)
    comp_item = Items.objects.get(pk = select_complete)
    comp_item.completed = False
    comp_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

