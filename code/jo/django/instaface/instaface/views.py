from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['text', 'caption', 'photo', 'poster']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['text', 'caption']

    # def test_func(self):
    #     post = self.get_object()
    #     return self.request.user == post.author
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    # def test_func(self):
    #     obj = self.get_object()
    #     return self.request.user == obj.author