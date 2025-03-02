from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from .models import Certificate
from .forms import CertificateForm
from django.contrib import messages

class CreateViewCreateView(CreateView):
    form_class = CertificateForm 
    template_name = 'upload_certificate/certificate_form.html'

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request,'correctly submitted')
        else:messages.error(self.request,'try again')

        return super().form_valid(form)
    

class CertificateListView(ListView):
    model = Certificate
    template_name = 'certificate.html'
    context_object_name = 'certificate'
    