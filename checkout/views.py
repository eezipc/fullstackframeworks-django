from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Userorders, SingleOrder
from products.models import Product
from basket.orders import basketorders

import stripe

# Create your views here.

def checkout(request):

    stripepublickey = settings.STRIPEPUBLICKEY
    stripesecretkey = settings.STRIPESECRETKEY
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'firstname': request.POST['firstname'],
            'lastname': request.POST['lastname'],
            'emailaddress': request.POST['emailaddress'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postalcode': request.POST['postalcode'],
            'town': request.POST['town'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'county': request.POST['county'],

        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    
                    order_line_item = SingleOrder(
                            order=order,
                            product=product,
                            amount=item_data,
                        )
                    order_line_item.save()
                    
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('basketview'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('confirmcheckout', args=[order.orderid]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            

    
    else:



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


def confirmcheckout(request, orderid):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Userorders, orderid=orderid)
    messages.success(request, f'Order successfully processed! \
        Your order number is {orderid}. A confirmation \
        email will be sent to {order.emailaddress}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/confirmcheckout.html'
    context = {
        'order': order,
    }

    return render(request, template, context)