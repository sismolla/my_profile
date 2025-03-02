
from .models import Contact_me ,Comment
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_me

        fields = [
            'name', 'email', 'phone_number', 'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(123) 456-7890'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here...', 'style': 'height: 10rem'}),
        }
