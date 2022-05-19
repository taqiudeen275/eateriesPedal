import imp
from unittest import signals
from django.db import models
from django.db.models.signals import post_save
from accounts.models import User
from vendor.models import Food


class FoodCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.food.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_cart")
    foodcart = models.ManyToManyField(FoodCart, related_name='inCart')
    total = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.user} Order List'

