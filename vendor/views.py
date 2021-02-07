from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Vendor


def become_vebdor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('core:landing_page')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'vendor/become_vendor.html', context)


def vendor_admin(request):
    vendor = request.user.vendor

    context = {
        'vendor': vendor
    }
    return render(request, 'vendor/vendor_admin.html', context)
