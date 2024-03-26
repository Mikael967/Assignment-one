from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def home(request):
    
    return render(request,'products/products.html')

def store(request):
    context = {}
    return render(request, 'Tugule/Tugule.html')

def cart(request):
    context = {}
    return render(request, 'Tugule/cart.html')

def checkout(request):
    context = {}
    return render(request, 'Tugule/checkout.html')