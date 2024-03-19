from django.contrib import admin
from . models import *

# Registering models
admin.site.register (Business_account)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

