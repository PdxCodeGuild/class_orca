from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random
import string

from .models import url


def index(request):
    return render(request, 'urlgen_app/index.html')
    # Notice that this only renders the TEMPLATE index.html 

def add_item(request):
    new_url = request.POST['new_url']
    library = string.ascii_letters + string.digits
    new_short = ''.join((random.choice(library) for i in range(5)))
    url.objects.create(url_long=new_url, url_short=new_short) 
    temp = url.objects.filter(url_short=new_short)
    print(temp)
    return HttpResponseRedirect(reverse('urlgen_app:index'))

def re_direct(request, url_id):
    response = "You're looking at the results of a redirect to %s."
    print(request)
    print(url_id)
    return HttpResponse(response % url_id)  
 

