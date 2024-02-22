"""
Module to use signals to save a profile
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	"""
	This is a function that creates a profile when a user is created.
	It uses the signal function to create a profile for the newly created user
	with the help of the receiver decorator
	"""
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	"""
    This is a function that saves the instance of the profile created
    """
	instance.profile.save()