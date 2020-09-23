import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.


class Userorders(models.Model):
    orderid = models.CharField(max_length=50, null=False, editable=False)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    emailaddress = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postalcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    orderdate = models.DateTimeField(auto_now_add=True)
    delivery = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    finaltotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _createorderid(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

     
    def updateorder(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.total = self.singleorder.aggregate(Sum('singleordertotal'))['singleordertotal__sum']
        if self.total < settings.FREEDELIVERY:
            self.delivery = self.total * settings.DELIVERYPERCENT / 100
        else:
            self.delivery = 0
        self.finaltotal = self.total + self.delivery
        self.save()

     
    def saveorder(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.orderid:
            self.orderid = self._createorderid()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.orderid



class SingleOrder(models.Model):
    order = models.ForeignKey(Userorders, null=False, blank=False, on_delete=models.CASCADE, related_name='singleorder')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False, default=0)
    singleordertotal = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def savesingleorder(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.singleordertotal = self.product.price * self.amount
        super().save(*args, **kwargs)


    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.orderid}'