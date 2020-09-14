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


def product_detail(request, product_id):
    """ Show single items in the shop """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }


    return render(request, 'products/shopping_detail.html', context)