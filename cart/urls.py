from django.urls import path
from .views import *

app_name = "cart"
urlpatterns = [
    path('add-to-cart/<str:food_url>', add_to_cart, name="add_to_cart"),
    path('add-to-cart/', add_to_cartView, name="cartAdd"),
    path('list', cartList, name="home"),
]