from django.http import HttpResponse, HttpResponseRedirect
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
    new_url = "http://127.0.0.1:8000/url_changer/"
    for x in range(5):
        new_url += random.choice(characters)
    url = UrlChanger.objects.create(long_url=input_url,short_url=new_url)
    context = {'url':url}
    return render(request, 'url_changer/index.html', context)
    return HttpResponseRedirect(reverse('url_changer:index'))

def redirect(request):
    # url_list = UrlChanger.
    # print(url_list)
    # current_url = resolve(request.path_info).url_name
    # print(current_url)
    # if current_url[-5:] in url_list:
    #     response = redirect('long_url')
    # print(response)

    # return response
    return HttpResponseRedirect(reverse('url_changer:index'))


