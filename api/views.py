from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]