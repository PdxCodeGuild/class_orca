from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import LongUrlShortCode

import string
import random

def index(request):
    url_item = 'You have not entered a long URL'
    context = {
        'url_item': url_item
    }
    return render(request, 'url_app/index.html', context)

def submit(request):
    #GET LONG URL FROM FORM.POST IN INDEX.HTML
    long_url = request.POST['LongCode']
    #MAKE SHORT CODE
    short_code = ''
    while len(short_code) < 6:
        short_code += random.choice(string.hexdigits)
    #CREATE NEW OBJECT IN DATABASE
    LongUrlShortCode.objects.create(long_url=long_url, short_code=short_code)
    #CREATE CONTEXT TO BE PASSED TO INDEX IE: DATA FOR INDEX
    context = {
        'long_url':long_url,
        'short_code':short_code
    }
    #RETURN INDEX PAGE WITH NEW OBJECT
    return render(request, 'url_app/index.html', context)
    

def redirect(request, url_code):
    redirect = LongUrlShortCode.objects.get(url_code=url_code) 
    redirect.url_counter += 1
    redirect.save()
    return HttpResponseRedirect(redirect.url) 

