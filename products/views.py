from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def allshopitems(request):
    """ Show all items in the shop """

    products = Product.objects.all()

    
    searchterm = None
    searchcategories = None

    """ Category Search query """
    if request.GET:
        if 'category' in request.GET:
            searchcategories = request.GET['category'].split(',')
            products = products.filter(category__name__in=searchcategories)
            searchcategories = Category.objects.filter(name__in=searchcategories)

    """ Search bar query """
    if request.GET:
        if 'q' in request.GET:
            searchterm = request.GET['q']
            if not searchterm:
                messages.error(request, "You didn't search for any item")
                return redirect(reverse('products'))

            searchterms = Q(name__icontains=searchterm) | Q(description__icontains=searchterm)
            products = products.filter(searchterms)



    context = {
        'products': products,
        'search_term': searchterm,
        'search_categories': searchcategories,
    }


    return render(request, 'products/shopping.html', context)


def product_detail(request, product_id):
    """ Show single items in the shop """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }


    return render(request, 'products/shopping_detail.html', context)