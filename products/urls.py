from django.urls import path
from . import views
app_name="products"
urlpatterns=[
    path('',views.home,name="home"),
    path('order/<str:product_id>',views.create_order_item,name="order"),
    path('cart/',views.cart,name="cart"),
    path('delete_order/<str:product_id>',views.deleteOrder,name="delete_order"),
  
]