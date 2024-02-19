from django.shortcuts import render, redirect

# Create your views here.
def landing_page(request):
    """
    This is the view to display the landing page
    """
    page = 'landing'
    context = {
        'title': 'Home',
    }
    return render(request, 'mysecret/landing.html', context)


def profile_home(request):
    """
    This is the view to display the user's profile after successful login.
    User must successfully login to access this page.
    """
    page = 'home'
    context = {
        'title': 'Profile'
    }
    return render(request, 'mysecret/profile.html', context)


def about_page(request):
    """
    This is the view to display the about page. It does not require
    login to access.
    """
    page = 'about'
    context = {
        'title': 'About'
    }
    return render(request, 'mysecret/about.html', context)


def contact_page(request):
    """
    This is the view to display the Contact page. It does not require
    login to access.
    """
    page = 'contact'
    context = {
        'title': 'Contact'
    }
    return render(request, 'mysecret/contact.html', context)


def signin_user(request):
    """
    This is the view to display the Login page.
    """
    page = 'login'
    context = {
        'title': 'Sign In'
    }
    return render(request, 'mysecret/login.html', context)


def signup_user(request):
    """
    This is the view to display the Registration page.
    """
    page = 'signup'
    context = {
        'title': 'Sign Up'
    }
    return render(request, 'mysecret/register.html', context)