from django import forms
from django.forms import widgets
from .models import ContactModel


class ContactForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'required': True, 'type': 'date'}))

    class Meta:
        model = ContactModel
        exclude = ['created_at', 'updated_at']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your email'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your year'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your location'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your mobile number'}),
            'study_location': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Enter your study location'}),
        }
