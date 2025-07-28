from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,pagination,filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailabletimeSerializer,RatingsSerializer
from .models import Doctor,Specialization,Designation,Availabletime,Ratings
# Create your views here.

class SpecicdoctorFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get('doctor_id')
        if doctor_id:
            
                return queryset.filter(doctor=doctor_id)
        return queryset



class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    def get_queryset(self):
        queryset= super().get_queryset()
        
        doctor_id=self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset    
class SpecializationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class =SpecializationSerializer
    queryset = Specialization.objects.all()
    
class RatingsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = RatingsSerializer
    queryset = Ratings.objects.all()
    
class DesignationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DesignationSerializer
    queryset = Designation.objects.all()

class Doctorpagination(pagination.PageNumberPagination):
    page_size = 1 #1pae e 1ta
    page_size_query_param = 'page_size'
    max_page_size = 5   
    
    
class AvailabletimeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AvailabletimeSerializer
    queryset = Availabletime.objects.all()
    pagination_class =  Doctorpagination
    filter_backends = [SpecicdoctorFilterBackend]
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI
from .models import Doctor
from .serializers import DoctorSerializer
from decouple import config
class SmartDoctorSearchAPIView(APIView):
    def post(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "No query provided"}, status=400)

        prompt = f"""
        A user is trying to find a doctor based on this input:
        "{query}"

        Extract only the medical specialization they need. Example outputs:
        - "eye"
        - "dental"
        - "cardiology"
        - "pediatric"
        - "dermatology"
        """

        try:
            client = OpenAI(api_key=config('OPENAI_API_KEY'))
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=15
            )
            keyword = response.choices[0].message.content.strip().lower()
        except Exception as e:
            return Response({'error': 'OpenAI failed', 'details': str(e)}, status=500)

        doctors = Doctor.objects.filter(
            specialization__icontains=keyword
        ) | Doctor.objects.filter(
            bio__icontains=keyword
        )

        serializer = DoctorSerializer(doctors, many=True)
        return Response({
            "keyword": keyword,
            "results": serializer.data
        })
