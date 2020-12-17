# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app

# from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
