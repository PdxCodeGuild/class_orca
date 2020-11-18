from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import random
import string

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
    return HttpResponseRedirect(url_redirect)


