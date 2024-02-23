from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (UserRegistrationForm, UserUpdateForm, ProfileUpdateForm,
                    NewSecretForm)
from django.contrib.auth.decorators import login_required
from mysecret.models import Secret
from django.contrib.auth.models import User
import uuid
from django.core.paginator import Paginator


def is_valid_id(uid):
    """
    This is a special function that is used to check if the ID presented is a
    valid ID:
    Args:
        uid (string): the uuid4 id to very
    Return:
        Bool - True if valid else false
    """
    try:
        uuid_obj = uuid.UUID(uid)
        return True
    except ValueError:
        return False


# Create your views here.
def register(request):
    """
    This is the route rendered for the User Registration process
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was successfully created. Please login.')
            return redirect('sign_in')
    else:
        form = UserRegistrationForm()
    context = {'form': form, 'title': 'Sign Up'}
    return render(request, 'users/register.html', context)


@login_required
def profile_home(request):
    """
    This is the route that is rendered when a user successfully log in.
    It shows all the secrets the user has. User needs to be logged in
    to access this page.
    """
    secret_list = Secret.objects.filter(author=request.user)

    paginator = Paginator(secret_list, 5)
    page_number = request.GET.get('page')
    secrets = paginator.get_page(page_number)
    context = {
        "title": 'Profile',
        'secrets': secrets
    }
    return render(request, 'users/home.html', context)


@login_required
def profile_details(request):
    """
    This is the route that is rendered showing the users profile for update.
    User needs to be logged in to access this page.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                             "Profile details updated successfully!")
            return redirect('profile_page')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'Profile Update',
        'profile_form': profile_form,
        'user_form': user_form
    }
    return render(request, 'users/profile.html', context)


@login_required
def secret_details(request, sid):
    """
    This is the route that is rendered showing details of a selected secret.
    User needs to be logged in to access this page.
    """
    if not is_valid_id(sid):
        messages.warning(request, "That ID provided is invalid!")
        return redirect('profile_page')

    try:
        secret = Secret.objects.get(secret_id=sid)
    except Secret.DoesNotExist:
        messages.warning(request, "That secret does not exist")
        return redirect('profile_page')

    context = {
        'title': secret.secret_title.title(),
        'secret': secret
    }
    return render(request, 'users/secret_details.html', context)


@login_required
def new_secret(request):
    """
    This is the route that is rendered to add a new secret to the DB.
    User needs to be logged in to access this page.
    """
    if request.method == 'POST':
        form = NewSecretForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Your secret was successfully saved.")
            return redirect('profile_page')
    else:
        form = NewSecretForm()
    context = {
        'title': 'New Secret',
        'form': form,
        'back_url': request.META.get('HTTP_REFERER')
    }
    return render(request, 'users/new_secret.html', context)


@login_required
def secret_update(request, sid):
    """
    This is the route that is rendered to update/modify a specified secret.
    User needs to be logged in to access this page.
    """
    if not is_valid_id(sid):
        messages.warning(request, "That ID provided is invalid!")
        return redirect('profile_page')
    
    try:
        secret = Secret.objects.get(secret_id=sid)
    except Secret.DoesNotExist:
        messages.warning(request, "That secret does not exist")
        return redirect('profile_page')

    if request.user.username == secret.author.username:
        if request.method == 'POST':
            form = NewSecretForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['secret_title']
                content = form.cleaned_data['secret_content']
                secret.secret_title = title.title()
                secret.secret_content = content
                secret.save()
                messages.success(request, "Your secret was successfully updated.")
                return redirect('profile_page')
        else:
            form = NewSecretForm(initial={'secret_title': secret.secret_title,
                                          'secret_content': secret.secret_content})
        context = {
            'title': 'Modify Secret',
            'form': form,
            'back_url': request.META.get('HTTP_REFERER')
        }
        return render(request, 'users/new_secret.html', context)
    else:
        messages.warning(request, "You are not authorized to modify this secret.")
        return redirect('profile_page')


@login_required
def confirm_secret_delete(request, sid):
    """
    This is the route that is rendered to confirm delete of a specified secret
    User needs to be logged in to access this page.
    """
    if not is_valid_id(sid):
        messages.warning(request, "That ID provided is invalid!")
        return redirect('profile_page')
    
    try:
        secret = Secret.objects.get(secret_id=sid)
    except Secret.DoesNotExist:
        messages.warning(request, "That secret does not exist")
        return redirect('profile_page')

    if request.user.username == secret.author.username:
        context = {
            'title': 'Delete Secret',
            'back_url': request.META.get('HTTP_REFERER'),
            'secret': secret
        }
        return render(request, 'users/secret_delete.html', context)
    else:
        messages.warning(request, "You are not authorized to delete this secret.")
        return redirect('profile_page')


@login_required
def delete_secret(request, sid):
    """
    This is the route that is rendered to delete a specified secret.
    User needs to be logged in to access this page.
    """
    if not is_valid_id(sid):
        messages.warning(request, "That ID provided is invalid!")
        return redirect('profile_page')
    
    try:
        secret = Secret.objects.get(secret_id=sid)
    except Secret.DoesNotExist:
        messages.warning(request, "That secret does not exist")
        return redirect('profile_page')

    if request.user.username == secret.author.username:
        secret.delete()
        messages.success(request, "Your secret was successfully deleted.")
        return redirect('profile_page')
    messages.warning(request,
                     'Could not delete the secret at this time. Try again')
    return redirect('profile_page')
