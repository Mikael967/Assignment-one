from django.forms import ModelForm
from .models import *



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ( 'name', 'product_caetegory','price')  

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
               

