from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
# from rest_framework import permissions
from rest_framework.permissions import AllowAny
# Create your views here.

class RegisterApiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]    
