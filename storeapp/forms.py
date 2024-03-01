from django import forms
from django.forms import ModelForm
from storeapp.models import User, Purchase
# from django.core.exceptions import ValidationError



class UserCreationForm(ModelForm):
    error_messages = {'password_mismatch': "The two password fields didn't match.",}
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ('username',)

    def cleen_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_message['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class PurchaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)
        # print('PurchaseForm __init__ user: ', self.current_user)
        # print('kvargs:')
        # print(kwargs)
        # print('Product id:',kwargs['data'])
        # print('aa:', self.data)
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = Purchase
        fields=('product_amount',)
    
    def clean_product_amount(self):
        product_amount=self.cleaned_data.get('product_amount')
        print(self.cleaned_data)
        # print('PurchaseForm clean_product_amount user: ', self.current_user)
        # print('\n I am cleen_product_amount')
        # print('product_amount: ', product_amount)
        # print(product_amount>3)
        # if product_amount>3:
        #     print('Hi from if')
        #     raise forms.ValidationError('product_amount>3')
        # return product_amount


        if product_amount>30:
            print('Hi from if')
            raise forms.ValidationError('product_amount>3')
        return product_amount
    
    def clean(self):
        print('\n I am cleen')
        print(self.data)
        print(self.data['productID'])

        cleaned_data = super().clean()