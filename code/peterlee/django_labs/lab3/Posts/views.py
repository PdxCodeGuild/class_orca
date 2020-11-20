from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'index.html')

def create(request):
    pass

def edit(request):
    pass

def delete(request):
    pass

