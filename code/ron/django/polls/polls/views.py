# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Choice, Question

def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question number {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at results of question number {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question number {question_id}.")
