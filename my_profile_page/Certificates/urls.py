from django.urls import path
from .views import CreateViewCreateView,CertificateListView

app_name = 'Certificates'

urlpatterns = [
    path('certificate_form/',CreateViewCreateView.as_view(),name='certificate_form'),
    path('certificate/',CertificateListView.as_view(),name='certificate'),
]