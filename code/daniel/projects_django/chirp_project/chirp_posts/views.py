from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import ChirpPosts

class PostListView(ListView):
    model = ChirpPosts 
    template_name = 'home.html'

class NewPostView(CreateView):
    model = ChirpPosts
    fields = ['author', 'title', 'content']
    template_name = 'new.html'
    
class PostDetailView(DeleteView):
    model = ChirpPosts
    template_name = 'detail.html'

class PostEditView(UpdateView):
    model = ChirpPosts
    fields = ['title', 'content']
    template_name = 'edit.html'

class DeletePost(DeleteView):
    model = ChirpPosts
    success_url = reverse_lazy('chirp_posts:home')
    template_name = 'delete.html'
