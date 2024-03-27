from django.shortcuts import render,redirect
from tugulenga.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


#views to create cart items
def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete = False)
        items = order.orderitem_set.all()
    else:    
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 
               'order':order}
    return render(request,"products/cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, complete = False)
        items = order.orderitem_set.all()
    else:    
        items=[]
        order ={'get_cart_total':0,'get_cart_items':0}
    context = {'items':items, 
               'order':order}
    return render(request,"", context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['product_id']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item,created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        order_item.quantity = (order_item.quantity+1)
    elif action == "remove":
        order_item.quantity = (order_item.quantity-1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse(action + ' complete', safe=False)



@login_required(login_url='tugule:login')
def home(request):
    categories = Category.objects.all()
    

    context={ "categories":categories}

    return render(request,'products/products.html',context)
@login_required(login_url='tugule:login')
def products(request,category_id):
    
    category=Category.objects.get(id=category_id)
    products=Product.objects.filter(category=category)
    context = {'category':category,'products':products,}
    return render(request,'products/category.html',context)

@login_required(login_url='tugule:login')


@login_required(login_url='tugule:login')
def deleteOrder(request,product_id):
    order=OrderItem.objects.get(id=product_id)
    if request.method=='POST':
        order.delete()
        return redirect('products:cart')
    context={"order":order}

    return render(request,'products/delete.html',context)

