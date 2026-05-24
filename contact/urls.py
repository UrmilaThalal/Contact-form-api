from django.urls import path
from .views import create_contact, get_contacts

urlpatterns = [
    path('contact/', create_contact),
    path('contacts/', get_contacts),
]