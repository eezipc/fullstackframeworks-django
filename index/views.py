from django.shortcuts import render

from django.http import HttpResponse

from .forms import ContactForm

from django.core.mail import send_mail


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n".format((sender_name, form.cleaned_data['message'])+(sender_name, form.cleaned_data['email']))
            send_mail('Message from EeziMotorcycles', message, sender_email, ['eezipc@gmail.com'])
            return render(request, 'index/success.html')
    else:
        form = ContactForm()

    return render(request, 'index/contact.html', {'form': form})
