from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(default='default.png', upload_to='avatars')

	def __str__(self):
		return f"Profile: {self.user.username}"


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.avatar.path)
		if img.height > 450 or img.width > 450:
			output_size = (450, 450)
			img.thumbnail(output_size)
			img.save(self.avatar.path)
