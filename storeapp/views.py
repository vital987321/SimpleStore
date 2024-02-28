from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, FormView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreationForm, PurchaseForm
from .models import Product, Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Register(CreateView):
    form_class=UserCreationForm
    template_name='register.html'
    success_url='/'

class Login(LoginView):
    success_url='/'
    template_name='login.html'

    def get_success_url(self):
        return self.success_url
    
class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


# class IndexView(LoginRequiredMixin, ListView):
#     template_name='index.html'
#     login_url = 'login/'
#     model=Product
#     # paginate_by=10
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = PurchaseForm()
#         return context


# class PurchaseView(CreateView):
#     form_class=PurchaseForm
#     template_name='purchase.html'
#     success_url=reverse_lazy('purchase')

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.client = self.request.user
#         obj.product = Product.objects.get(pk=form.data['productID'])
#         obj.save()
#         return super().form_valid(form=form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # print('\n get_context_data:')
#         # print(context['form'].data)
#         return context


class IndexView(LoginRequiredMixin, ListView):
    template_name='index.html'
    login_url = 'login/'
    model=Product
    # paginate_by=10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PurchaseForm()
        return context


class PurchaseView(CreateView):
    
    template_name='purchase.html'
    success_url=reverse_lazy('purchase')
    form_class=PurchaseForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client = self.request.user
        obj.product = Product.objects.get(pk=form.data['productID'])
        obj.save()
        return super().form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('\n get_context_data:')
        # print(context['form'].data)
        return context

class MyOrdersView(LoginRequiredMixin, ListView):
    template_name = 'myorders.html'
    login_url = 'login/'
    model = Purchase


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = PurchaseForm()
    #     return context

class ReturnView(DeleteView):
    model=Purchase
    success_url = reverse_lazy('myorders')
