from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basketorders(request):

    itemsinbasket = []
    totalamount = 0
    productamount = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        totalamount += item_data * product.price
        productamount += item_data
        itemsinbasket.append({
            'item_id': item_id,
            'amount': item_data,
            'product': product,
        })

    if totalamount < settings.FREEDELIVERY:
        finaldelivery = totalamount * Decimal(settings.DELIVERYPERCENT / 100)
        freedeliveryupdate = settings.FREEDELIVERY - totalamount
    else:
        finaldelivery = 0
        freedeliveryupdate = 0
    
    finaltotal = finaldelivery + totalamount
    
    context = {
        'itemsinbasket': itemsinbasket,
        'totalamount': totalamount,
        'productamount': productamount,
        'finaldelivery': finaldelivery,
        'freedeliveryupdate': freedeliveryupdate,
        'freedelivery': settings.FREEDELIVERY,
        'finaltotal': finaltotal,
    }

    return context