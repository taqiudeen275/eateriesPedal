from django.shortcuts import redirect, render,get_object_or_404
from vendor.models import Food
from django.http import JsonResponse
from .models import FoodCart,Cart
from django.contrib.auth.decorators import login_required
import json

@login_required
def cartList(request):
    user = request.user
    cartItems = Cart.objects.filter(user=user)[0]
    context = {
        'title': 'My Cart',
        'cart_items': cartItems,
    }
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, food_url):
    if request.method == "POST":
        user = request.user
        food = get_object_or_404(Food, food_url= food_url)
        if not user.my_cart.exists():
            cart = Cart.objects.create(user=user)
        cart = Cart.objects.get(user=user)
        quantity = request.POST.get('quantity')
        foodcart = FoodCart.objects.create(food=food, quantity=quantity, user=user)
        cart.foodcart.add(foodcart)
        return redirect('cart:home')
    else:
        return redirect('home:menu')

@login_required
def add_to_cartView(request):
    data = json.loads(request.body)
    food_id = data['product']
    action = data['action']
    user = request.user
    food = get_object_or_404(Food, id= food_id)
    if action == "add":
        if not user.my_cart.exists():
            cart = Cart.objects.create(user=user)
        cart = Cart.objects.get(user=user)
        FoodCart.objects.get_or_create(food=food, user=user)
        foodcart = FoodCart.objects.get(food=food, user=user)
        if foodcart.inCart.exists():
            foodcart.quantity += 1
            foodcart.save()
            
            print("found")
        else:
            foodcart.quantity = 1
            foodcart.save()
            cart.foodcart.add(foodcart)
            cart.save()
    else:
        cart = Cart.objects.get(user=user)
        foodcart = cart.foodcart.get(food=food_id, user=user)
        if foodcart.quantity <= 1:
            foodcart = FoodCart.objects.get(food=food_id, user=user)
            foodcart.delete()
        foodcart.quantity -= 1
        foodcart.save()
    cart_item = Cart.objects.get(user=user)
   
    total = 0
    for fooditem in cart_item.foodcart.all():
        total += (fooditem.food.price * fooditem.quantity)
    cart_item.total = total
    cart_item.save()

                

    return JsonResponse('It was added', safe=False)
