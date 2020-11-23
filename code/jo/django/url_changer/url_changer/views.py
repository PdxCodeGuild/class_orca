from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, resolve

import random
import string

from .models import UrlChanger

def index(request):
    return render(request, 'url_changer/index.html')


def convert(request):
    input_url = request.POST['long_url']
    characters = string.ascii_letters + string.digits
    new_url = ""
    for x in range(5):
        new_url += random.choice(characters)
    url = UrlChanger.objects.create(long_url=input_url,short_url=new_url)
    context = {'url':url}
    return render(request, 'url_changer/index.html', context)
    return HttpResponseRedirect(reverse('url_changer:index'))


def redirect(request, short_url):
    code = get_object_or_404(UrlChanger, short_url=short_url)
    code.ip = request.META['REMOTE_ADDR']
    code.clicked += 1
    code.linked_from = request.META['HTTP_REFERER']
    code.save()
    return HttpResponseRedirect(code.long_url)
