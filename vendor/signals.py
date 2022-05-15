from venv import create
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Food
import random
import string


def food_urls_generator(foodname):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    foodname = foodname.replace(" ", "-")
    urls_string = f"{foodname}-{result_str}"
    return urls_string

@receiver(pre_save, sender=Food)
def user_info_handler(sender,instance,*args, **kwargs):
    if instance:
        url = food_urls_generator(instance.name)
        instance.food_url = url
