from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput({ "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput({ "placeholder": "Email Address"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 35, "placeholder": "Enter Your Message Here"}))