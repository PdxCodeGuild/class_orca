from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import urlCode

import string, random 

def index(request):
    url_database = urlCode.objects.all()
    context = {'url_database': url_database,} 
    return render(request, 'url_shortner_app/index.html', context) 


def url_source(request):
    url_address = request.POST['url_address']
    url_code = url_code_generator()
    url_name = request.POST['url_name']
    urlCode.objects.create(url_code=url_code, url_name=url_name, url=url_address)
    return HttpResponseRedirect(reverse('url_shortner_app:index'))

def url_code_generator():
    url_code = []
    characters = list(string.ascii_letters + string.digits +  string.punctuation)
    for x in range(6):
        url_code.append(random.choice(characters))
    url_code = ''.join(url_code) 
    return url_code 

def user_redirect(request, url_code):
    redirect = urlCode.objects.get(url_code=url_code) 
    print(redirect.url) 
    return HttpResponseRedirect(redirect.url)


