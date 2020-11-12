from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.

def index (request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(latest_question_list)

def detail(request, question_id):
    return HttpResponse("You're looking at question number {question_id}")

def results(request, question_id):
    return HttpResponse("You're looking at results question number {question_id}")

def vote(request, question_id):
    return HttpResponse("You're voting on question number {question_id}")

  


