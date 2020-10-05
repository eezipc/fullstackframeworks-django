from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def allshopitems(request):
    """ Show all items in the shop """

    products = Product.objects.all()
    searchterm = None
    searchcategories = None
    sort = None
    direction = None

    
    if request.GET:

        """ Sort by category, rating or price """
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        """ Category Search query """
        if 'category' in request.GET:
            searchcategories = request.GET['category'].split(',')
            products = products.filter(category__name__in=searchcategories)
            searchcategories = Category.objects.filter(name__in=searchcategories)

        """ Search bar query """
        if 'q' in request.GET:
            searchterm = request.GET['q']
            if not searchterm:
                messages.error(request, "You didn't search for any item")
                return redirect(reverse('products'))

            searchterms = Q(name__icontains=searchterm) | Q(description__icontains=searchterm)
            products = products.filter(searchterms)

    page_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': searchterm,
        'search_categories': searchcategories,
        'page_sort': page_sort,
    }


    return render(request, 'products/shopping.html', context)


def product_detail(request, product_id):
    """ Show single items in the shop """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }


    return render(request, 'products/shopping_detail.html', context)

def new_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added a new product')
            return redirect (reverse('new_product'))
        else:
            messages.error(request, 'Oops, something does not look right. Check the form again')
    else:
        form = ProductForm()

    template = 'products/new_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product to the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have edited a product')
            return redirect (reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something does not look right. Check the form again')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are now editing {product.name}')
        
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))