from django.urls import path

from .views import (become_vendor, vendor_admin, add_product_to_vendor)

app_name = 'vendor'

urlpatterns = [
    path('become-vendor', become_vendor, name='become_vendor'),
    path('vendor-admin', vendor_admin, name='vendor_admin'),
    path('add-product', add_product_to_vendor, name='add_product_to_vendor'),
]
