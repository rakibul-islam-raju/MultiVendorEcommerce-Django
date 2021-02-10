import random

from django.shortcuts import render, get_object_or_404

from .models import Product, Category


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
    product = get_object_or_404(
        Product, 
        pk=pk,
        category__category_slug=category_slug,
        product_slug=product_slug
    )

    similar_products = list(Product.objects.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    context = {
        'product': product,
        'similar_products': product
    }
    
    return render(request, 'product/product_detail.html', context)

