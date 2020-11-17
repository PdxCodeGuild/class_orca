# POLLS EXAMPLE PROJECT

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader # don't need this anymore
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # context object name

    def get_queryset(self):
        '''
        returns the last five published questions, not including those set for the future
        '''
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        '''
        excludes any questions that are not published yet
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#  COMMENTED OUT FUNCTION-BASED VIEWS:
# def index(request):
#     # we want a landing page with a list of polls
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html') # remember this is in templates/xxx folder, in this case 'polls'
#     context = {'latest_question_list': latest_question_list}
#     # output = ', '.join([q.question_text for q in latest_question_list])    
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404(f"Question {question_id} does not exist. 404.")

#     # replaced above by importing: get_object_or_404 and writing below:
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # POST MUST be in ALL CAPS
    except (KeyError, Choice.DoesNotExist):
        # philosophy of doing BOTH error checkinf...
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice. Please try again."
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # trailig comma necessary for tuple, could be a list with one [thing]