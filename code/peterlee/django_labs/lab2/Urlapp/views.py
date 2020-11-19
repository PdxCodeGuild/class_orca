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
        entry = Bank.objects.get(original_url=request.POST['entry'])
        return HttpResponseRedirect(reverse('Urlapp:results', args=(entry.id,)))
    else:
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for x in range(6))
        new_entry = Bank(new_code=code, original_url=request.POST.get('entry'))
        new_entry.save()
        return HttpResponseRedirect(reverse('Urlapp:results', args=(new_entry.id,)))

def results(request, pk):
    entry = get_object_or_404(Bank, pk=pk)
    code = entry.new_code
    original_url = entry.original_url
    context = {'code':code, 'original_url':original_url}
    return render(request, 'Urlapp/results.html', context)

def short(request, code):
    entry = get_object_or_404(Bank, new_code=code)
    b = entry.original_url
    if b.startswith('https://'):
        return HttpResponseRedirect(b)
    else:
        c = 'https://' + b
        return HttpResponseRedirect(c)