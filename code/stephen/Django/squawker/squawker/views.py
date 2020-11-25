from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Squeek

class SqueekListView(ListView):
    model = Squeek
    template_name = "home.html"
    
class SqueekDetailView(DetailView):
    model = Squeek
    template_name = 'squeek_detail.html'

class SqueekCreateView(LoginRequiredMixin, CreateView):
    model = Squeek
    template_name = 'squeek_new.html'
    fields = ['title', 'photo', 'post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SqueekEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Squeek
    template_name = 'squeek_edit.html'
    fields = ['title', 'photo', 'post']

    def test_func(self):
        squeek = self.get_object()
        return self.request.user == squeek.author

class SqueekDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Squeek
    template_name = 'squeek_delete.html'
    success_url = reverse_lazy('squawker:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
