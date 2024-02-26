from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm

class Register(CreateView):
    form_class=UserCreationForm
    template_name='register.html'
    success_url='/'

class Login(LoginView):
    success_url='/'
    template_name='login.html'

    def get_success_url(self):
        return self.success_url
