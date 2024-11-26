from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]