from django.shortcuts import render

# TODO: Create login_view and add logical redirection

def landing_page(request):
    return render(request, 'landing-page.html')
