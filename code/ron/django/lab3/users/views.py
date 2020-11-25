from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/sign_up.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'users/user_profile.html'

    # What does this do exactly?
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])