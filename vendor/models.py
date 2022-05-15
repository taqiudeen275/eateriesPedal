from pyexpat import model
from django.db import models
from accounts.models import User



class VendorAcount(models.Model):
    user = models.ForeignKey(User, related_name='vendor', on_delete=models.CASCADE, blank=True, null=True)
    business_name = models.CharField(max_length=255)
    photo = models.ImageField(default="profile/logo.png",  upload_to='profile/')
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    contact_2 = models.CharField(max_length=15, null=True, blank=True)
    ratings = models.BigIntegerField(default=0)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.business_name
    
class Food(models.Model):
    vendor = models.ForeignKey(VendorAcount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='food-img/')
    price = models.IntegerField()
    offer = models.CharField(max_length=255, null=True, blank=True)
    ratings = models.IntegerField(default=0)
    delivery_time = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1024)
    food_url = models.CharField(max_length=255, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.name