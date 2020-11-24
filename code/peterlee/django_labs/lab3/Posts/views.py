from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from .models import Posts


def index(request):
    posts = Posts.objects.all()
    context = {'Posts':posts}
    return render(request, 'index.html', context)

def detail(request):
    return

def create(request):
    return

def edit(request):
    return

def delete(request):
    return

