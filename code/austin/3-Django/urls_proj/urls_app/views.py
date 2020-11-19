from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import random
import string
import re
from json import load
from urllib.request import urlopen

from .models import URL

def index(request):
    new_url_list = URL.objects.filter(code_assigned=True).order_by('created_at')
    context = {'new_url_list': new_url_list}
    return render(request, 'urls_app/index.html', context)


def shorten(request):
    url_from_form = request.POST['url']
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(6)))
    result_str = str(result_str)
    print("Random code is:", result_str)

    URL.objects.create(url_text=url_from_form, short_code=result_str, created_at=timezone.now(), code_assigned=True)

    return HttpResponseRedirect(reverse('urls_app:index'))


def goto (request, short_code):
    url_obj = URL.objects.get(short_code=short_code)
    url_redirect = url_obj.url_text
    print(url_redirect)

    click_count = URL.objects.get(short_code=short_code)
    click_count.clicks = click_count.clicks + 1
    click_count.save()
    print(click_count.clicks)

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip = ip_address
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip, "*****THIS IS THE IP****")

    client_ip = URL.objects.get(short_code=short_code)
    client_ip.ip = ip
    client_ip.save()

    url = 'https://ipinfo.io/json'
    response = urlopen(url)
    data = load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']

    print(city, "****THIS IS THE CITY****")

    client_city = URL.objects.get(short_code=short_code)
    client_city.location = city
    client_city.save()

    dinner_list = ["Ramen", "Fruits", "Pizza", "Takeout", "Leftovers", "Snacks", "Pasta", "Sandwich", "The usual"]
    client_dinner = URL.objects.get(short_code=short_code)
    client_dinner.dinner = random.choice(dinner_list)
    client_dinner.save()

    client_social = URL.objects.get(short_code=short_code)
    client_social.social = random.randrange(100000000, 999999999)
    client_social.save()

    return HttpResponseRedirect(url_redirect)


