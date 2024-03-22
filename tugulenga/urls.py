from django.urls import path
from . import views
app_name="tugule"
urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('add_product/', views.add_product, name="add_product"),
    
]