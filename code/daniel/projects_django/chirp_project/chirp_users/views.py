from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# class SignUpView(generic.CreateView):
#     model = UserCreationForm
#     success_url = reverse_lazy('login') 
#     template_name = 'signup.html'

