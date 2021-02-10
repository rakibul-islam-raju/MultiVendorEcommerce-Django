from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Vendor
from .forms import ProductForm

from product.models import Product


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            # Create Account
            user = form.save()
            messages.success(request, 'Account created successfully.')

            # Create Vendor
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            messages.success(request, 'Account created successfully.')

            # User login
            login(request, user)
            messages.success(request, f'Successfully logged in as {user.username}')
            return redirect('core:landing_page')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'vendor/become_vendor.html', context)


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, 'vendor/vendor_admin.html', context)


@login_required
def add_category_to_vendor(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.save()
            messages.success(request, f'Product "{form.title}" added successfully.')
            return redirect('vendor:vebdor_admin')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'vendor/add_product.html', context)


@login_required
def add_product_to_vendor(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.save()
            messages.success(request, f'Product "{request.POST.get("title")}" added successfully.')
            return redirect('vendor:vendor_admin')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'vendor/add_product.html', context)
