
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()