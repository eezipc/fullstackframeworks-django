from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userphone = models.CharField(max_length=20, null=True, blank=True)
    usercountry = CountryField(blank_label='Country *', null=True, blank=True)
    userpostalcode = models.CharField(max_length=20, null=True, blank=True)
    usertown = models.CharField(max_length=40, null=True, blank=True)
    useraddress1 = models.CharField(max_length=80, null=True, blank=True)
    useraddress2 = models.CharField(max_length=80, null=True, blank=True)
    usercounty = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()