from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    return HttpResponse(latest_question_list)

def detail(request, question_id):
    return HttpResponse(f"you're looking at question number {question_id}.")

def results(request, question_id):
    return HttpResponse(f"you're looking at the resultes of question number {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"you're voting on question number {question_id}.")