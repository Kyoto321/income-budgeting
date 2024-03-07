from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)
    
    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        
        if not first_name.isalnum():
            raise serializers.ValidationError('Name must not not contain numbers')
        
        if not last_name.isalnum():
            raise serializers.ValidationError('Name must not not contain numbers')
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=1000)
    
    class Meta:
        model = User
        fields = ['token']
        
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=100, read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name','tokens']
        
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid email and password. Try again')
        
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        
        
        
        return {
            'email':user.email,
            'first_name': user.first_name,
            'tokens': user.tokens()
        }

        return super().validate(attrs)
        
        
class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    
    class Meta:
        fields = ['email']
        

        

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=55, min_length=6, write_only=True)
    token = serializers.CharField(min_length=3, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields=['password', 'token', 'uidb64']
        
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            
            user.set_password(password)
            user.save()
            
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        
        return super().validate(attrs)