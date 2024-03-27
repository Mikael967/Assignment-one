from django.urls import path
from . import views
app_name="products"
urlpatterns=[
    path('',views.home,name="home"),
    
    path('cart/',views.cart,name="cart"),
    path('delete_order/<str:product_id>',views.deleteOrder,name="delete_order"),
    path('category/<str:category_id>', views.products, name='category'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/',views.checkout,name="checkout"),
  
]