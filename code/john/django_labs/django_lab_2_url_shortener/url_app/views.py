# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse

import string, random # to generate_short_code for the short URL code:

from .models import URL

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

    context = {
        'url_address': url,
        'short_code': short_code,
    }

    print(f'>>>>>PRINT: FUNCTION RUNNING: generate_short_code... pairing url {url} with {short_code}.')
    print(f'>>>>>PRINT: request.path : {request.path}.')
    print(f'>>>>>PRINT: request.body : {request.body}.') # this is kinda the 'raw' URL entered, with &url=stuff entered into form here
    # print(f'>>>>>PRINT: request.__dir__() : {request.__dir__()}.') # BIG, but only a few lines, mostly blank in this ex
    # print(f'>>>>>PRINT: request.__dict__  : {request.__dict__ }.') # MASSIVE, ~2 pages... see test.py for an example of whole return
    # print(f'>>>>>PRINT: request.META : {request.META}.') # BIG, 
    print(f'>>>>>PRINT: request.path_info : {request.path_info}.')
    print(f'>>>>>PRINT: request.GET : {request.GET}.')
    print(f'>>>>>PRINT: request.POST : {request.POST}.')
    # print(f'>>>>>PRINT: request.META : {request.META}.')
    print(f'>>>>>PRINT: request.headers : {request.headers}.')
        # EXAMPLE
        # uncomment this for a better view:
        # request.headers : {
        #     'Content-Length': '89', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': '127.0.0.1:8000', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 
        #     'Origin': 'http://127.0.0.1:8000', # # # #   maybe
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 
        #     'Referer': 'http://127.0.0.1:8000/', # # # #   maybe
        #     'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 
        #     'Cookie': 'csrftoken=3MP1JSTbTB6abnhLEeUabKSOfsDT5hJqccFo04F1LINbmzivR1barXovVbElqCzx; sessionid=8a6q5z7g089ew2c1kcgjq2yiq9jzul73' # # # #  maybe
        #     }
    print(f'>>>>>PRINT: request.get_host() : {request.get_host()}.')
    # print(f'>>>>>PRINT: request.build_absolute_uri(location=None) : {request.build_absolute_uri(location=None)}.') # target URL address

    return render(request, 'url_app/display_short_code.html', context) # what to send to that URL


def redirect_code_to_URL(request, code): # MIGHT NOT NEED 'REQUEST' HERE...

    print(f'>>>>>PRINT: FUNCTION RUNNING: redirect_code_to_URL,  with request {request} and short_code {code}.')
    print(f'>>>>>PRINT: request.path : {request.path}.')
    print(f'>>>>>PRINT: request.body : {request.body}.')
    print(f'>>>>>PRINT: request.path_info : {request.path_info}.')
    print(f'>>>>>PRINT: request.GET : {request.GET}.')
    # print(f'>>>>>PRINT: request.headers : {request.headers}.') 

    url_target = get_object_or_404(URL, short_code=code)
    print(f'>>>>>PRINT: url_target : {url_target}.')
    
    return HttpResponseRedirect(url_target.url_address)

# TODO could put logic that redirects non http or https://

# EXAMPLE REDIRECT CODES:
# bAx1IA8g to https://johnfial.github.io/
# WgmNMUa6 to https://raw.githubusercontent.com/PdxCodeGuild/class_orca/main/3%20Django/docs/django_request_response_cycle.png
# sxI2jZBL to https://docs.djangoproject.com/en/3.1/intro/tutorial01/