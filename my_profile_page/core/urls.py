from django.urls import path
from .views import HomerView,ContactView,DirectContact

app_name = 'core'

urlpatterns = [
    path('',HomerView.as_view(),name='index'),
    path('contact/',DirectContact.as_view(),name='contact'),
    path('direct_contact/',ContactView.as_view(),name='direct_contact'),

]