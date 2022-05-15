from .forms import *
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User

@login_required
def vendorRegister(request):
    vform = VendorForm(request.POST or None,  request.FILES)
    user = request.user
    if user.user_type == 'Consumer':
        return redirect('home:index')
    if request.method == "POST":
        if vform.is_valid():
            print(dir(vform))
            form = vform.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('vendor:profile')
    context = {
        'form': vform,
        'title': "Vendor Account Registration",
    }
    template_name = 'vendor-register.html'
    return render(request, template_name, context)

@login_required
def vendorProfiileView(request):
    user = request.user
    if user.user_type == 'Consumer':
        return redirect('home:index')
    vendor = get_object_or_404(VendorAcount, user=request.user)
    template_name = 'profile.html'
    context = {
        'title': f"{vendor.business_name} Profile",
        'vendor': vendor,

    }
    return render(request, template_name, context)

@login_required
def foodaddView(request):
    user = request.user
    if user.user_type == 'Consumer':
        return redirect('home:index')
    form = FoodForm(request.POST or None, request.FILES)
    print(dir(request.user.vendor))
    if request.method == "POST":
        if form.is_valid():
            iform =form.save(commit=False)
            iform.vendor = get_object_or_404(VendorAcount, user=request.user)
            iform.save()
            return redirect('home:menu')
    template_name = 'foodAdd.html'
    context = {
        'title': 'Add Food',
        'form': form,

    }
    return render(request, template_name, context)
