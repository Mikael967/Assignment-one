from django.shortcuts import render
from tugulenga.models import Product
# Create your views here.
def home(request):
    products=Product.objects.all()
    context={"products":products}
    
    return render(request,'products/products.html',context)
