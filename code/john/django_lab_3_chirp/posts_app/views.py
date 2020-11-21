# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app

# django urls stuff
from django.shortcuts import render
from django.urls import reverse_lazy

# django views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# django auth stuff
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# our post model
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'

    fields = ['post_text' ] # add 'photo' if media

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # CreateView has a form_valid() function...
        # super means ... before you do what you were going to do anyway... let me add something

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['post_text']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url = reverse_lazy('posts_app:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author



