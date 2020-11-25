from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random
import string

from .models import url

 
def index(request):
    return render(request, 'urlgen_app/index.html')
    # Notice that this only renders the TEMPLATE index.html, does not pass data

def add_item(request):
    new_url = request.POST['new_url']
    library = string.ascii_letters + string.digits
    new_short = ''.join((random.choice(library) for i in range(5)))
    url.objects.create(url_long=new_url, url_short=new_short)
    new_url = url.objects.get(url_short = new_short)
    context = {
        'new_url': new_url
    }
    # print(context)
    return render(request, 'urlgen_app/index.html', context)
    # return HttpResponseRedirect(reverse('urlgen_app:index'))

def re_direct(request, url_short):
    website1 = url.objects.get(url_short = url_short)
    return HttpResponseRedirect(f'https://{website1}')


 

