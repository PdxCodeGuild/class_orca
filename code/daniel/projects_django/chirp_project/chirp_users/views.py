from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login') 

class UserProfile(generic.DetailView):
    model = User          # context_object_name = somenameinstead
    template_name = 'profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username']) 