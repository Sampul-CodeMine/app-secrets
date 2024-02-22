from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


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
	context = {
		"title": 'Profile',
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
