

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer,RegistrationSerializer
from .models import Patient
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
from django.core.mail import EmailMultiAlternatives

class Registrationview(APIView):
    serializer_class=RegistrationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request).domain
            verification_link = f"http://{current_site}/patient/verify-email/{uid}/{token}/"
            subject = "Verify your email"
            email_body=render_to_string('confirm_email.html',{'confirmation_link':verification_link})
            msg = EmailMultiAlternatives(subject,'', to=[user.email])
            msg.attach_alternative(email_body, "text/html")
            msg.send()
            print(user)
            return Response("Please check your email")
        
        return Response(serializer.errors)
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

class VerifyEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except Exception as e:
            return Response({'error': 'Invalid link'}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Email verified successfully!'})
        else:
            return Response({'error': 'Invalid or expired token'}, status=400)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if not user.is_active:
                return Response({"error": "Please verify your email first."}, status=403)

            # আগের সব টোকেন ডিলিট করে ফেলুন
            Token.objects.filter(user=user).delete()

            # নতুন টোকেন তৈরি করুন
            token = Token.objects.create(user=user)

            login(request, user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)

    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

class LogoutView(APIView):
    def get(self, request):  # GET method handle করা হলো
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logout successful"}, status=200)
