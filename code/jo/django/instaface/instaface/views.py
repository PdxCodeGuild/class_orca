from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

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
    fields = ['text', 'caption', 'photo']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['text', 'caption']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.poster
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('instaface:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.poster

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

# class LargeImageView():
#     model = Post