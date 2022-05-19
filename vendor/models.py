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

reiview_choice = [
    (1, '1 Trash'),
    (2, '2 Horible'),
    (3, '3 Terrible'),
    (4, '4 Manageable'),
    (5, '5 Good'),
    (6, '6 Better'),
    (7, '7 Tasty'),
    (8, '8 Yummy'),
    (9, '9 Awesome'),
    (10, '10 Superb'),
]

class FoodReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='myreview')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='review')
    rate = models.PositiveSmallIntegerField(choices=reiview_choice, null=True, blank=True)
    text = models.TextField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return f'{self.food} review'

class FoodAverageRatings(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="averageRating")
    rate = models.PositiveSmallIntegerField(default=0)