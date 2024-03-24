from django.shortcuts import render,redirect
from tugulenga.models import Product,Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.
def create_order_item(request,product_id):
     
    order=Order.objects.create(customer =  request.user)
    order.save()
    product=Product.objects.get(id=product_id)
    

   
    
 
    #check if order item already in database
    try:
        same_item=OrderItem.objects.get(product=product)
        same_item.quantity+=1
        same_item.save()

    except: 
        order_item=OrderItem.objects.create(
        product=product,
        order=order,
        quantity=1,)
        order_item.save()
    
        
        
    


    return redirect('products:home')
@login_required(login_url='tugule:login')
def home(request):
    products=Product.objects.all()
    context={"products":products}

    return render(request,'products/products.html',context)

@login_required(login_url='tugule:login')
def cart(request,):
    order_items=OrderItem.objects.all()
    context={"order_items":order_items}
    return render(request,'products/cart.html',context)

@login_required(login_url='tugule:login')
def deleteOrder(request,product_id):
    order=OrderItem.objects.get(id=product_id)
    if request.method=='POST':
        order.delete()
        return redirect('products:cart')
    context={"order":order}

    return render(request,'products/delete.html',context)

