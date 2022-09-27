from django import forms
from .models import Contact
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'specialty', 'publication', 'email', 'phone']
        labels = {
            'id': 'ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'specialty': 'Specialty',
            'publication': 'Publication',
            'email': 'Email Address',
            'phone': 'Phone Number'
        }

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'publication': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': PhoneNumberPrefixWidget(initial='US'),
        }