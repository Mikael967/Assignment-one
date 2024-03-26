from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image','category','name','price']

class Business_accountForm(ModelForm):
    class Meta:
        model = Business_account
        fields = '__all__'  

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields = '__all__'  

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

class  CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email','password1', 'password2']
