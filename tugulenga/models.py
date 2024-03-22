from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Creating  models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One to one relationship with the User model.
    # image = models.ImageField(default='avatar.png', upload_to= 'profile/', blank=True)
    contact = models.CharField(max_length = 50, default='07893672948')
    name = models.CharField(max_length = 200, default = user)

  
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
    #save the profile
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size =(300,300)
        #     img.thumbnail(output_size)
        #     img.save (self.image.path)

    


class Business_account(models.Model):

    owner= models.OneToOneField(User,on_delete= models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length =20)
    email = models.EmailField()
    location = models.CharField(max_length = 255)
    description = models.TextField()
    logo = models.ImageField(upload_to='Logos/', null= True, blank=True)
    

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
    image = models.ImageField( upload_to="Products/",blank=True)
    product_category=models.CharField(max_length=20, choices=Product_category.choices, default=Product_category.Services)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete= models.CASCADE, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False, null=True,blank =False)
    

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product 
    


    





     
    