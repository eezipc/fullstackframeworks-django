from decimal import Decimal
from django.conf import settings

def basketorders(request):

    itemsinbasket = []
    totalamount = 0
    productamount = 0

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