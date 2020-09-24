from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import SingleOrder

@receiver(post_save, sender=SingleOrder)
def updateonsave(sender, instance, created, **kwargs):
# Line below may be incorrect. Check later. Userorders may be orders (or something else)
    instance.Userorders.updateorder()

@receiver(post_delete, sender=SingleOrder)
def deleteonsave(sender, instance, **kwargs):
# Line below may be incorrect. Check later. Userorders may be orders (or something else)
    instance.Userorders.updateorder()
