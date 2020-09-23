from django import forms
from .models import Userorders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Userorders
        fields = ('firstname', 'lastname', 'emailaddress', 'phone',
                  'address1', 'address2', 'town', 'county',
                   'postalcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'emailaddress': 'Email Address',
            'phone': 'Phone Number',
            'address1': 'Address',
            'address2': 'Address',
            'town': 'Town',
            'county': 'County',
            'postalcode': 'Postal Code',
            'country': 'Country',
                        
        }

        self.fields['firstname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False