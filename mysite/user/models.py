from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=30)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=30)
    country = models.CharField(blank=True, max_length=30)
    image = models.ImageField(blank=True, upload_to='images/user/')


    def __str__(self):
        return f'{self.user.username}'

    def user_name(self):
        return f'{self.user.first_name} ({self.user.last_name}) ({self.user.username})'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'