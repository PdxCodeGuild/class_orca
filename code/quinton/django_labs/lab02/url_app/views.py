from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import LongUrlShortCode

import string, random


def index(request):
    return render(request, 'url_app/index.html')

def add_url(request):
    print(request.POST)
    return HttpResponse('Hi')

def url_gen():
    password = ''
    while len(password) < 6:
        password += random.choice(string.hexdigits)
    return password
