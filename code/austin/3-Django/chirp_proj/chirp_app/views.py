from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'chirp_app/index.html', {})

def blog(request):
    return render(request, 'chirp_app/blog.html', {})

def post(request):
    return render(request, 'chirp_app/post.html', {})
