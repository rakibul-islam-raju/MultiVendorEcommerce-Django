from django.urls import path

from .views import (product_list, product_detail, category, search_product)

app_name = 'product'

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/<slug:category_slug>/<slug:product_slug>/',
        product_detail, name='product_detail'),
    path('products/<slug:category_slug>/', category, name='category'),
    path('search/', search_product, name='search_product'),
]
