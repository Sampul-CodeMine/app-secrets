"""
This is a module that is used to create a new user, update users' profile
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """
    This is a class to provide the User Registration form
    It inherits from the UserRegistrationForm provided by Django
    """
    email = forms.EmailField()

    class Meta:
        """
        This is a meta class to define the fields to be rendered bt the form,
        using the User model for its definition
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    This is a class to provide the User Update form
    It inherits from the forms class provided by Django
    """
    email = forms.EmailField()

    class Meta:
        """
        This is a meta class to define the fields to be rendered bt the form,
        using the User model for its definition
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    This is a class to provide a form to update the avatar of a User's profile.
    It inherits from the forms class provided by Django
    """
    class Meta:
        model = Profile
        fields =  ['avatar']
