from django.http import HttpResponse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    return HttpResponse("Hello World")

def detail(request, question_id):
    return HttpResponse(f"This is question number {question_id}.")

def results(request, question_id):
    return HttpResponse(f"Results of question number {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question number {question_id}.")



