from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import ContactUs
# Create your views here.
class ContactusViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()
    
   