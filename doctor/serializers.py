from rest_framework import serializers
from .models import Doctor,Specialization,Designation,Ratings,Availabletime
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization= serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    availabletime = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'
class AvailabletimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabletime
        fields = '__all__'
class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'