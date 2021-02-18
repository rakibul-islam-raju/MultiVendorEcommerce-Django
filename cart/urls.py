from django.urls import path

from .views import (cart_detail)

app_name = 'cart'

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
]
