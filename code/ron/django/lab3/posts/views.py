
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# import db info from models
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'posts/index.html'

class BlogDetailView(DetailView):           #, CreateView
    model = Post
    template_name = 'posts/post_show.html'

class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'posts/post_new.html'
    # fields = ['__all__']                  # specifies all fields for creation
    fields = ['title', 'body','photo']             

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogEditView(UpdateView, LoginRequiredMixin, UserPassesTestMixin ):             
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ['title', 'body']
    # fields = ['__all__']

    def test_func(self):
        obj = self.get_object()
        # What does this code do?  Returns t/f if author == self? 
        return self.request.user == obj.author

class BlogDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin): 
    model = Post
    template_name = 'posts/post_delete.html'
    # Note: reverse_lazy tells the system to not automatically excute (used for classes vs. functions)
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        obj = self.get_object()
        # What does this code do?  Returns t/f if author == self?
        return self.request.user == obj.author

# test views
# def index(request):
#     return render(request, 'posts/index.html')
