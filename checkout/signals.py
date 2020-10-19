from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import SingleOrder


@receiver(post_save, sender=SingleOrder)
def updateonsave(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.updateorder()


@receiver(post_delete, sender=SingleOrder)
def deleteonsave(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.updateorder()
