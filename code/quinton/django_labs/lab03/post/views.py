from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello world. You're at the home page")

def detail_view(request, tweet_id):
    return HttpResponse("You're looking at tweet %s." % tweet_id)


