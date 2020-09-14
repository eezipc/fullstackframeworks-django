from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def allshopitems(request):
    """ Show all items in the shop """

    products = Product.objects.all()

    context = {
        'products' : products,
    }


    return render(request, 'products/shopping.html', context)