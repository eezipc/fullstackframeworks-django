from django.shortcuts import render

# Create your views here.
""" Show the index page """
def basketview(request):
    return render(request, 'basket/basket.html')