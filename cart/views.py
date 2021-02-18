from django.shortcuts import render, redirect
from django.contrib import messages
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart')
    change_quantity = request.GET.get('change_quantity')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        messages.warning(request, 'Item was removed from your cart.')
        return redirect('cart:cart_detail')

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart:cart_detail')

    return render(request, 'cart/cart.html')
