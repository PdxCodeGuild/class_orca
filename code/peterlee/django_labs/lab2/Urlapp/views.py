from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
import random
import string

from .models import Bank


def index(request):
    return render(request, 'Urlapp/index.html')

def shorten(request):
    if Bank.objects.filter(original_url=request.POST['entry']).exists():
        entry = Bank.objects.get(original_url=request.POST.get('entry'))
        code = entry.new_code
        return HttpResponseRedirect(reverse('Urlapp:results', args=(code,)))
    else:
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for x in range(6))
        new_entry = Bank(new_code=code, original_url=request.POST.get('entry'))
        new_entry.save()
        return HttpResponseRedirect(reverse('Urlapp:results', args=(code,)))

def results(request, context):
    context = context
    return render(request, 'Urlapp/results.html', context)