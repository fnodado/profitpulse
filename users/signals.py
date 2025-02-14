from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal to create a Profile when a User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,
            username=instance.username,
            email=instance.email,
            first_name = instance.first_name)
        print(f"Profile created for user {instance.username}")

# Signal to save Profile when User is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
