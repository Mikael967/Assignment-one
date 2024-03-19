from django.db import models
from django.contrib.auth.models import User

# Creating  models here.
class Customer (models.Model):
    name = models.CharField(max_length =100)
    email=models.EmailField()
    

    def __str__(self):
        return self.name
    


class Business_account(models.Model):

    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length =20)
    email = models.EmailField()
    location = models.CharField(max_length = 255)
    description = models.TextField()
    
    

    def __str__(self):
        return self.name
    
class Product(models.Model):
    class Product_category(models.TextChoices):
        supermarket = 'supermarket', 'supermarket'
        home_and_office = 'home_and_office','home_and_office'
        electronics = 'electronics','electronics'
        Health_and_beauty = 'Health_and_beauty','Health_and_beauty'
        fashion = 'fashion','fashion'
        Computing = 'Computing','Computing'
        sporting_goods = 'sporting_goods','sporting_goods'
        garden_and_outdoors = 'garden_and_outdoors','garden_and_outdoors'
        food = 'food ','food '
        gaming = 'gaming ','gaming '
        vehicle = 'vehicle','vehicle'
        Services = 'Services','Services'

    business_account= models.ForeignKey(Business_account, on_delete=models.CASCADE, null=True, blank=True )
    product_category=models.CharField(max_length=20, choices=Product_category.choices, default=Product_category.Services)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete= models.CASCADE, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False, null=True,blank =False)
    transaction_id =models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    


    





     
    