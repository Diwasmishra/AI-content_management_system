from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['role'] = user.role
        token['name'] = user.name
        token['is_staff'] = user.is_staff
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra info in response body (frontend can access this)
        data['role'] = self.user.role
        data['name'] = self.user.name
        data['is_staff'] = self.user.is_staff
        data['email'] = self.user.email
        data['user_id'] = self.user.id

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True}  # Prevent clients from setting role on user creation

        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def create(self, validated_data):
        # hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

