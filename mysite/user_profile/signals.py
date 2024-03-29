from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from . models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_profile(instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)
    if hasattr(instance, 'auth_token'):
        instance.auth_token.save()
    else:
        Token.objects.create(user=instance)
