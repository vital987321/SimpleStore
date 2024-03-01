from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, FormView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreationForm, PurchaseForm
from .models import Product, Purchase, User
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
        productID=form.data['productID']
        obj.product = Product.objects.get(pk=productID)
        stock_amount=obj.product.stock_amount
        quantyty=int(form.data['product_amount'])
        print('\n form_valid')
        if quantyty <= stock_amount:
            if obj.product.price*quantyty<obj.client.wallet:
                Product.objects.filter(id=productID).update(stock_amount=stock_amount-quantyty)
                # obj.client.wallet=obj.client.wallet-quantyty*obj.product.price
                # obj.client.save()
                User.objects.filter(id=obj.client.id).update(wallet=obj.client.wallet-quantyty*obj.product.price)
                obj.save()
                return super().form_valid(form=form)
            else:
                print('!!! Client does not have enouph money')
        else:
            print('!!! Not enoupg products in stock')        
        return super().form_invalid(form=form)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MyOrdersView(LoginRequiredMixin, ListView):
    template_name = 'myorders.html'
    login_url = 'login/'
    model = Purchase


class ReturnView(DeleteView):
    model=Purchase
    success_url = reverse_lazy('myorders')
