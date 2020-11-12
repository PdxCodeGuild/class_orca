from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question 

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published questions not including those set to be published in the future'''
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5] 
    
class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/details.html'

    def get_queryset(self):
        '''Excludes any questions that are not published yet'''
        return Question.objects.filter(pub_date__lte=timezone.now()) 
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html' 

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # (-) returns the most recent question # [:5] only returns the most five recent ones
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)                          

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id) 
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist.")
#     ###because imported get_object_or_404 we can condense code to below
#     question = get_object_or_404(Question, pk=question_id) 
#     return render(request, 'polls/detail.html', {'question': question}) 

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): 
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice. Please try again."
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 

