from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import random
import string

from .models import Shortener

def index(request):
    return render(request, 'url_short_app/index.html')

def convert_url():
    letters = string.ascii_letters
    token = ''.join(random.choice(letters) for x in range(6))
    print(token)
    return token


def submit_long(request):
    url = Shortener.objects.create(long_url=request.POST['long_url'], short_url=convert_url())
    context = {'short_url': url.short_url}
    return render(request, 'url_short_app/index.html', context)

def redirect_url(request, token):
    long_url = Shortener.objects.filter(short_url = token)[0]
    return HttpResponseRedirect (long_url.long_url)
