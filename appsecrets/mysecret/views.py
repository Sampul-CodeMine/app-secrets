from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
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
    form = ContactForm()
    context = {
        'title': 'Contact', 'form': form
    }
    return render(request, 'mysecret/contact.html', context)


def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            admin_email = settings.ADMIN_EMAIL[0] if isinstance(settings.ADMIN_EMAIL, list) else settings.ADMIN_EMAIL

            context = {
                'admin': admin_email,
                'name': name,
                'email': email,
                'msg': message
            }
            html_message = render_to_string('mysecret/includes/email_template.html', context)
            plain_message = strip_tags(html_message)


            try:

                send_mail(
                    subject,
                    plain_message,
                    email,
                    [admin_email],
                    fail_silently=False,
                    html_message=html_message,
                )
                messages.success(request, "Your message was successfully sent")
                return redirect('contact_page')
            except Exception as e:
                messages.warning(request, f"An error occured while sending your message: {e}")
                return redirect('contact_page')
    else:
        form = ContactForm()
    return redirect('contact_page')