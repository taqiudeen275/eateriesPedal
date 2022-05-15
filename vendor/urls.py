from django.urls import path
from .views import *

app_name = "vendor"
urlpatterns = [
    path('register', vendorRegister, name='register'),
    path('profile', vendorProfiileView, name="profile"),
    path('food-add', foodaddView, name="foodAdd"),
]