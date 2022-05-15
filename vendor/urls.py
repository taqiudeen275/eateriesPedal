from django.urls import path
from .views import *

app_name = "vendor"
urlpatterns = [
    path('register', vendorRegister, name='register'),
    path('profile-update', vendorProfileEdit, name='profileUpdate'),
    path('profile', vendorProfiileView, name="profile"),
    path('food-add', foodaddView, name="foodAdd"),
    path('food/<int:id>/Edit', foodEditView, name="foodEdit"),
    path('food/<int:id>/Delete', foodDeleteView, name="foodDelete"),
]