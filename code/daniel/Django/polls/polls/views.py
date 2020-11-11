from django.http import HttpResponse
from .models import Choice, Question 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # (-) returns the most recent question
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)                          # [:5] only returns the most five recent ones

def detail(request, question_id):
    return HttpResponse(f"You're looking at question number {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question number {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question number {question_id}.")

