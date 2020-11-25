from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Posts


def index(request):
    post_list = Posts.objects.all()
    context = {'post_list':post_list}
    return render(request, 'index.html', context)

def detail(request, pk):
    detailed_post = get_object_or_404(Posts, pk=pk)
    context = {'detailed_post':detailed_post}
    return render(request, 'detail.html', context)

@login_required
def delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.user == post.author:
        post.delete()
        return HttpResponseRedirect(reverse('Posts:index'))


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostsEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    template_name = 'edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



