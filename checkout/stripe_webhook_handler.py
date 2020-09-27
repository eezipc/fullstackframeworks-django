from django.http import HttpResponse
from .models import Userorders, SingleOrder
from products.models import Product

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        finaltotal = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Userorders.objects.get(
                    firstname__iexact=shipping_details.name,
                    emailaddress__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postalcode__iexact=shipping_details.address.postal_code,
                    town__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    finaltotal=finaltotal,
                    originalbasket=basket,
                    stripepid=pid,
                )
                order_exists = True
                break
            except Userorders.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Userorders.objects.create(
                    firstname=shipping_details.name,
                    emailaddress=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postalcode=shipping_details.address.postal_code,
                    town=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    originalbasket=basket,
                    stripepid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    
                    order_line_item = SingleOrder(
                            order=order,
                            product=product,
                            amount=item_data,
                        )
                    order_line_item.save()
                    
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)



    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)