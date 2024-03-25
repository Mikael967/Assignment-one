from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from .forms import CreateUserForm
from django.contrib import messages
from .decorators import unauthenticated_user
from .models import *

# Create your views here.
def home(request):
    
    return render(request,'tugulenga/index.html')

@unauthenticated_user   
def signup(request):
     
    form = CreateUserForm()
    if request.method=='POST':
        form =CreateUserForm(data=request.POST)
        if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')

                messages.success(request,'Account was created for'+ user)
                return redirect('tugule:login')
            
    context={"form":form}
    return render(request,"tugulenga/signup.html",context)
     
@unauthenticated_user     
def loginPage(request):
   
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password )
        if user is not None:
            login(request,user)
            return redirect('products:home')
        else:
            messages.info(request,'Username or Password is incorrect')
        
    return render(request,'tugulenga/login.html')

def logoutUser(request):
     logout(request)
     return redirect('tugule:home')

  
  
    
