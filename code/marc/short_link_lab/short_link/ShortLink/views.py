from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import random
import string

from .models import ShortLink

def index(request):
    context = {}
    return render(request, 'ShortLink/index.html', context)

def create_code(request):
    long_url = request.POST['long_url']
    character_choice = "f{string.ascii_lowercase} + {string.ascii_uppercase} + {string.digits}"
    short_url = random.choice(character_choice)
    while (len(short_url)) < 5:
        short_url = short_url + random.choice(character_choice)
    ShortLink.objects.create(url_link= long_url, short_url= short_url)
    print(short_url)
    context = {'short_url':short_url, 'long_url':long_url}
    return render(request, 'ShortLink/index.html', context)


def re_direct(request, short_url):
    new_link = get_object_or_404(ShortLink, short_url=short_url)
    return  HttpResponseRedirect(new_link.url_link)


    # return  HttpResponseRedirect(reverse('ShortLink:index'))

# def redirect(self, short_url):
#     get_object_or_404(GroceyItem, pk=complete_id)
#     return  HttpResponseRedirect(reverse('grocery_app:index'))


    
