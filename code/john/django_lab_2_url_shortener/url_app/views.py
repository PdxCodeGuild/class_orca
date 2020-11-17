# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse

# are these two necessary here, in models.py, or not at all?
# from django.utils import timezone
# import datetime

from .models import URL

# to generate_short_code for the short URL code:
import string
import random

def index(request):
    return render(request, 'url_app/index.html', {} )


def generate_short_code(request):

    characters = string.digits + string.ascii_letters
    short_code = ''
    while len(short_code) < 8:
        next_character = random.choice(characters)
        short_code += next_character

    url = request.POST['url']

    URL.objects.create(url_address=url, short_code=short_code)    
    print(f'>>>>>PRINT: generate_short_code RAN... pairing url {url} with {short_code}.')

    context = {
        'url_address': url,
        'short_code': short_code,
    }
    return render(request, 'url_app/display_short_code.html', context) # what to send to that URL


def redirect_code_to_URL(request, code): # MIGHT NOT NEED 'REQUEST' HERE...

        # EXAMPLE REDIRECT CODES:
        # bAx1IA8g to https://johnfial.github.io/
        # WgmNMUa6 to https://raw.githubusercontent.com/PdxCodeGuild/class_orca/main/3%20Django/docs/django_request_response_cycle.png
        # sxI2jZBL to https://docs.djangoproject.com/en/3.1/intro/tutorial01/

    print(f'redirect_code_to_URL with request {request} and short_code {code}.')
    url_target = get_object_or_404(URL, short_code=code)    
    
    return HttpResponseRedirect(url_target.url_address)


# TODO could put logic that redirects non http or https://