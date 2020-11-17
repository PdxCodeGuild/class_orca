from django.shortcuts import render
from django.http import HttpResponse

def testfunction(request):
    return HttpResponse('ok')