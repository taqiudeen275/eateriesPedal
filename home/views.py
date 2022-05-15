from django.shortcuts import render,get_object_or_404
from vendor.models import Food,VendorAcount
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count,Q


def indexView(request):
    context= {
        'title': "Eateries Pedal"
     }
    return render(request, 'index.html', context)

def aboutView(request):
    return render(request, 'about.html', context={'title': 'About'})

def menuView(request):
    foods = Food.objects.order_by('-time_stamp')
    paginator = Paginator(foods, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)

    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context={
        'title': 'Menu',
        'foods': paginated_qs,
        'rpv': page_request_var,
        }
    return render(request, 'menu.html', context)

def foodView(request, food_url):
    food = get_object_or_404(Food, food_url=food_url)
    foods = Food.objects.filter(vendor=food.vendor)
    context={
        'title': food,
        'food': food,
        'foods': foods,
        }
    return render(request, 'food.html', context)

def vendorProfileView(request, vendorID):
    vendor = get_object_or_404(VendorAcount, id=vendorID)
    context={
        'title': f'{vendor} Profile',
        'vendor': vendor,
        }
    return render(request, 'vendorProfile.html', context)

def foodSearchView(request):
    qs = Food.objects.all()
    q = request.GET.get('q')
    if q:
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(price__icontains=q)
        ).distinct()
    context = {
        'title': f"'{q}' search results",
        'results': qs,
        'q':q,
    }
    return render(request, 'search_results.html', context)
