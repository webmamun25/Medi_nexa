from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User 

import jwt
from django.conf import settings



class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'
        
        

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password','confirm_password']
        
    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password1=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        
        if password1!=confirm_password:
            raise serializers.ValidationError("Password doesn't match")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already exists')
        
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password1)
        account.save()
        return account 

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email','password','confirm_password']
        
    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password1=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        
        if password1!=confirm_password:
            raise serializers.ValidationError("Password doesn't match")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already exists')
        
        account=User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password1)
        account.is_active=False
        account.save()
        return account 
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)