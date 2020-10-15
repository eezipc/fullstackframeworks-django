from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Eezimotorcycles Views.
""" Show the index page """


def basketview(request):
    return render(request, 'basket/basket.html')


def updatebasketview(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    product = Product.objects.get(pk=item_id)
    amount = int(request.POST.get('amount'))
    redirectpage = request.POST.get('redirectpage')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += amount
        messages.success(request, f'Updated {product.name} amount to {basket[item_id]}')
    else:
        basket[item_id] = amount
        messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirectpage)


def changebasketview(request, item_id):

    product = Product.objects.get(pk=item_id)
    amount = int(request.POST.get('amount'))
    basket = request.session.get('basket', {})

    if amount > 0:
        basket[item_id] = amount
        messages.success(request, f'Updated {product.name} amount to {basket[item_id]}')
    else:
        del basket.pop[item_id]
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('basketview'))


def deletebasketview(request, item_id):

    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.success(request, f'Oops, something went wrong {e}')
        return HttpResponse(status=500)
