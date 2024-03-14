from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login ,logout

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
  
    
