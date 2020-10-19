from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact
from django import forms

""" Contact Form """


class ContactForm(ModelForm):
     class Meta:
        model = Contact
        fields = ["first_name", "last_name", "message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave Your Message Here"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name"
                }
            ),

        }
