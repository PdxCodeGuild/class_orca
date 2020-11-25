from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import ChirpPosts

class PostListView(ListView):
    model = ChirpPosts 
    template_name = 'home.html'

class NewPostView(LoginRequiredMixin, CreateView):
    model = ChirpPosts
    fields = ['title', 'content']
    template_name = 'new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class PostDetailView(DeleteView):
    model = ChirpPosts
    template_name = 'detail.html'

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ChirpPosts
    fields = ['title', 'content']
    template_name = 'edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ChirpPosts
    success_url = reverse_lazy('chirp_posts:home')
    template_name = 'delete.html'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

