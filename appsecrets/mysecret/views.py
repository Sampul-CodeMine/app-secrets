from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'mysecret/landing.html', context)