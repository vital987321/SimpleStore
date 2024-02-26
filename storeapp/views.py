from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreationForm
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

class Register(CreateView):
    form_class=UserCreationForm
    template_name='register.html'
    success_url='/'

class Login(LoginView):
    success_url='/'
    template_name='login.html'

    def get_success_url(self):
        return self.success_url
    

class IndexView(LoginRequiredMixin, ListView):
    template_name='index.html'
    login_url = 'login/'
    model=Product
    paginate_by=10



class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'
