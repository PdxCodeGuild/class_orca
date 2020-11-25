  
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import RagePage

class RagePageListView(ListView):
    model = RagePage
    template_name = 'home.html'

class RagePageDetailView(DetailView):
    model = RagePage
    template_name = 'ragepage_detail.html'

class RagePageCreateView(LoginRequiredMixin, CreateView):
    model = RagePage
    template_name = 'post_new.html'
    fields = ['title', 'photo', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RagePageEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RagePage
    template_name = 'post_edit.html'
    fields = ['title', 'caption']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author