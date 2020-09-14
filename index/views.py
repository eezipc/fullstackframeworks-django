from django.shortcuts import render

# Create your views here.
""" Show the index page """
def index(request):
    return render(request, 'index/index.html')