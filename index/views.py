from django.shortcuts import render

# Create your views here.
""" Show the index page """
def index(request):
    return render(request, 'index/index.html')

  
""" Show the contact page """
def contact(request):
    return render(request, 'index/contact.html')

""" Show the terms page """
def terms(request):
    return render(request, 'index/terms.html')

""" Show the privacy page """
def privacy(request):
    return render(request, 'index/privacy.html')

""" Show the success page """
def success(request):
    return render(request, 'index/success.html')