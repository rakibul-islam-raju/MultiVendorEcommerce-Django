from cart.forms import AddToCartForm
import random

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category

from cart.cart import Cart


def search_product(request):
    query = request.GET.get('product_query')
    products = Product.objects.filter(
        Q(title__icontains=query)
        | Q(description__icontains=query)
    )
    context = {
        'products': products,
        'qs_str': query
    }
    return render(request, 'product/search.html', context)


def category(request, category_slug):
    category = get_object_or_404(Category, category_slug=category_slug)
    context = {
        'category': category
    }
    return render(request, 'product/category.html', context)


def product_list(request):
    new_products = Product.objects.all()[0:8]
    context = {
        'new_products': new_products
    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, pk, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(
        Product, 
        pk=pk,
        category__category_slug=category_slug,
        product_slug=product_slug
    )

    if request.method == 'POST':
        form = AddToCartForm(request.POST or None)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(
                product_id=product.id,
                quantity=quantity
            )
        
        messages.success(request, f'{product.title} was added to your cart.')

        return redirect(
            'product:product_detail', 
            pk=product.pk, 
            category_slug=product.category.category_slug,
            product_slug=product.product_slug
        )
    else:
        form = AddToCartForm()

    similar_products = list(Product.objects.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    context = {
        'product': product,
        'similar_products': product,
        'form': form
    }
    
    return render(request, 'product/product_detail.html', context)

