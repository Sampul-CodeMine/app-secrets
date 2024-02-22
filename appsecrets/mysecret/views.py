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


def profile_page(request):
    """
    This is the view to display the logged in users profile
    """
    context = {
        'title': 'Profile',
        'secrets': Secret.objects.all()
    }
    return render(request, 'mysecret/profile.html', context)


def sign_up(request):
    """
    This is the view to display the Registration page for new users
    """
    context = {
    'title': 'Sign Up'
    }
    return render(request, 'mysecret/register.html', context)


def sign_in(request):
    """
    This is the view to display the Login page for old users
    """
    context = {
    'title': 'Sign In'
    }
    return render(request, 'mysecret/login.html', context)