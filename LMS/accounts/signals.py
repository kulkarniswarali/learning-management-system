from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User, Group 

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        

@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  