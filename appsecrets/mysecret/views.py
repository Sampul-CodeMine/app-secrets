from django.shortcuts import render, redirect
from .models import Secret


# Create your views here.
def landing_page(request):
    """
    This is the view to display the landing page
    """
    context = {
        'title': 'Home',
    }
    return render(request, 'mysecret/landing.html', context)


def about_page(request):
    """
    This is the view to display the about page. It does not require
    login to access.
    """
    context = {
        'title': 'About'
    }
    return render(request, 'mysecret/about.html', context)


def contact_page(request):
    """
    This is the view to display the Contact page. It does not require
    login to access.
    """
    context = {
        'title': 'Contact'
    }
    return render(request, 'mysecret/contact.html', context)
