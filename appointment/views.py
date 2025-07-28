
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    def get_queryset(self):
            queryset= super().get_queryset()
        
            patient_id=self.request.query_params.get('patient_id')

            if patient_id:
                queryset = queryset.filter(patient_id=patient_id)
            return queryset  