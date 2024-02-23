#!/usr/bin/python3
"""
This is a Script to define the database models
"""
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import uuid as uid


class Secret(models.Model):
    """
    This is the Secrets models to develop the secrets table in the database.
    It inherits from the Django models
    """
    secret_id = models.UUIDField(primary_key=True, default=uid.uuid4, editable=False)
    secret_title = models.CharField(max_length=120)
    secret_content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Secret {self.secret_id} ({self.secret_title})"

    def get_absolute_url(self):
        return reverse('secret_details', kwargs={'pk', self.ph})
