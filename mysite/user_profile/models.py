from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        verbose_name=("user"),
        on_delete=models.CASCADE,
        related_name="profile",
    )
    picture = models.ImageField(("picture"),
        upload_to='user_profile/img/',
        default='user_profile/img/default.jpg'
    )

    def __str__(self):
        return f'{str(self.user)} ("profile")'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        picture = Image.open(self.picture.path)
        if picture.height > 300 or picture.width > 300:
            output_size = (300, 300)
            picture.thumbnail(output_size)
            picture.save(self.picture.path)

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"
