from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from basket.orders import basketorders

import stripe

# Create your views here.

def checkout(request):

    stripepublickey = settings.STRIPEPUBLICKEY
    stripesecretkey = settings.STRIPESECRETKEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "The basket is empty")
        return redirect(reverse('products'))

    stripebasket = basketorders(request)
    stripetotal = stripebasket['finaltotal']
    finalstripetotal = round(stripetotal * 100)
    stripe.api_key = stripesecretkey
    intent = stripe.PaymentIntent.create(
        amount=finalstripetotal,
        currency=settings.STRIPE_CURRENCY,
    )

# Remove this when finished project

    print(intent)



    order_form = OrderForm()

    if not stripepublickey:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripepublickey' : stripepublickey,
        'client_secret': intent.client_secret,

 
    }

    return render(request, template, context)
