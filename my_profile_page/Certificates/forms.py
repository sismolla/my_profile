from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['issued_for', 'issued_date', 'link', 'image', 'description']
