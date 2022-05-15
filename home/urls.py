from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', indexView, name='index'),
    path('about', aboutView, name='about'),
    path('menu', menuView, name='menu'),
    path('food/<str:food_url>/details', foodView, name='food'),
    path('vendor/<int:vendorID>/profile', vendorProfileView, name='vendorProfile'),
    path('food-search', foodSearchView, name='foodSearch'),
    
]