from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from .forms import *
from .models import *

# Create your views here.
def home(request):
    
    return render(request,'tugulenga/index.html')

def signup(request):
    form = UserCreationForm()
    if request.method=='POST':
        form =UserCreationForm(data=request.POST)
        if form.is_valid():
             user =form.save()
             username = form.cleaned_data.get('username')
             raw_password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=raw_password)
             login(request,user)
             return home(request)
             
    context={"form":form}
    return render(request,"tugulenga/signup.html",context)
def login(request):
    if request.method == 'POST':
        
    
        
        username = request.POST.get('username')
        user = authenticate(username=username, password=request.POST.get('password'))
        login(request,user)
            #return redirect('/profile')
    return render(request,'tugulenga/login.html')
  
def add_product(request):
    business_account = Business_account.objects.get(owner = request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            product_category = form.cleaned_data['product_category']

            product = Product.objects.create(
                business_account = business_account,
                name = name,
                price = price,
                product_category = product_category
            )
            product.save()
            return redirect('products:home')
    else:
        form = ProductForm()

    return render(request, 'tugulenga/add_product.html',{'form':form})

def add_business_account(request):
    owner = Business_account.objects.get(owner = request.user)
    if request.method == 'POST':
        form = Business_accountForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            logo = form.cleaned_data['logo']


            business_product = Business_account.objects.create(
                owner = owner,
                name = name,
                phone = phone,
                email = email,
                location = location,
                description = description,
                logo = logo
            )
            business_product.save()
            return redirect('tugule:add_business_acoount')
    else:
        form = Business_accountForm()

    return render(request, 'tugulenga/add_business_account.html',{'form':form})

def add_orderItem(request):
    owner = Business_account.objects.get(owner = request.user)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.cleaned_data['product']
            order = form.cleaned_data['order']
            quantity = form.cleaned_data['quantity']
            

            order_item = OrderItem.objects.create(
                owner = owner,
               product = product,
               order = order,
               quantity = quantity,
              

            )
            order_item.save()
            return redirect('products:home')
    else:
        form = OrderItemForm()

    return render(request, 'tugulenga/add_orderItem.html',{'form':form})
