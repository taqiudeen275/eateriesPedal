from itertools import count
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Food,FoodAverageRatings,FoodReview
import random
import string


def food_urls_generator(foodname):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    foodname = foodname.replace(" ", "-")
    urls_string = f"{foodname}-{result_str}"
    return urls_string

@receiver(pre_save, sender=Food)
def food_url_handler(sender,instance,*args, **kwargs):
    if instance:
        FoodAverageRatings.objects.get_or_create(food=instance)

def averageratingsCalc(list_of_rates):
    total_rate = 0
    print(list_of_rates)
    n = len(list_of_rates)
    print(n)
    for rate in list_of_rates:
        total_rate += rate
    average = (total_rate) / n
    return average

@receiver(post_save, sender=FoodReview)
def average_rating(sender,created, instance,*args, **kwargs):
    if created:
        FoodAverageRatings.objects.get_or_create(food=instance.food)
        food = instance.food
        aveRating = FoodAverageRatings.objects.get(food=food)
        foodReview = FoodReview.objects.filter(food=food)
        rates = [x.rate for x in foodReview]
        avRate = averageratingsCalc(rates)
        aveRating.rate = avRate
        aveRating.save()



@receiver(post_save, sender=FoodAverageRatings)
def food_rating_handlar(sender,created, instance,*args, **kwargs):
     if instance:
        rfood = instance.food
        food = Food.objects.get(id=rfood.id)
        food.ratings = instance.rate
        food.save()
