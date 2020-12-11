from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Main
from django.http import HttpResponse, HttpResponseRedirect
import random
from string import ascii_letters, digits

def index(request):
    return render(request, 'app_lab_2/index.html')

def submit(request):
    url = request.POST['url_input']
    print(request.POST)
    code = random_code()
    url_obj = Main(url_text=url, code_text=code )
    # url_obj is now an object(variable) storing a url and code Ex: google.com 1538fw
    print(url_obj)
    url_obj.save()
    # this works too    Main.objects.create(url_text=url, code_text=code)
    # this is for before the redirect to code page    return HttpResponseRedirect(reverse('app_lab_2:index'))
    context = {'code_text': code}
    print('x' * 30)    
    print('x' * 30)   
    print('x' * 30)   
    print(request.META)
    print('x' * 30)    
    print('x' * 30)   
    print('x' * 30)   
    return render(request, 'app_lab_2/sucess.html', context)

def redirect_def(request, code):
    website = get_object_or_404(Main, code_text=code,)
    print(website)
    website.click_count += 1
    website.save()
    return redirect(website.url_text)

def random_code():
    string = ''
    letters_numbers = ascii_letters + digits
    for i in range(6):
        string += random.choice(letters_numbers)
    return string



