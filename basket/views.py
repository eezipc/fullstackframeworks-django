from django.shortcuts import render, redirect

# Create your views here.
""" Show the index page """
def basketview(request):
    return render(request, 'basket/basket.html')



def updatebasketview(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    amount = int(request.POST.get('amount'))
    redirectpage = request.POST.get('redirectpage')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += amount
    else:
        basket[item_id] = amount

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirectpage)