from django.shortcuts import render

from django.http import HttpResponse

from .forms import ContactForm

from django.core.mail import send_mail

from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy


# Create your views here.
""" Show the index page """


def index(request):
    return render(request, 'index/index.html')


""" Show the terms page """


def terms(request):
    return render(request, 'index/terms.html')


""" Show the privacy page """


def privacy(request):
    return render(request, 'index/privacy.html')


""" Show the success page """


def success(request):
    return render(request, 'index/success.html')



def contact(request):
    return render(request, 'index/contact_form.html')


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")

    
def thanks(request):
    return render(request, 'index/success.html')

