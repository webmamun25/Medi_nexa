from rest_framework import serializers
from .models import Appointment
class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField(many=False)
    doctor= serializers.StringRelatedField(many=False)
    availabletime = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appointment
        fields = '__all__'