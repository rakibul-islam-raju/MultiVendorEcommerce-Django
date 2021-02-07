from django.urls import path

from .views import (become_vebdor, vendor_admin)

app_name = 'vendor'

urlpatterns = [
    path('become-vendor', become_vebdor, name='become_vendor'),
    path('vendor-admin', vendor_admin, name='vendor_admin'),
]
