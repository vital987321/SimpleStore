from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm

class Register(CreateView):
    form_class=UserCreationForm
    template_name='register.html'
    success_url='/'