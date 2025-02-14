from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # Ensure this is imported

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the profile first

        if self.image and self.image.name != "default.jpg":  # Avoid processing default image
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)  # Resize and save the image
