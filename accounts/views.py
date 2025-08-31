from django.shortcuts import render


# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Login (get token)
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({
            "token": token.key,
            "user_id": token.user_id,
            "username": token.user.username
        })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "token": serializer.validated_data["token"],
            "user_id": serializer.validated_data["user"].id,
            "username": serializer.validated_data["user"].username
        })

# Logout (delete token)
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Logged out successfully."})

# Current user profile
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
