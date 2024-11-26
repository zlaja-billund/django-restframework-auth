from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

class UserLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = authenticate(email=data["email"], password=data["password"])

        # If not user found return status 401
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})