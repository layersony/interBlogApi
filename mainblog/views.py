from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .serializer import BlogSerializer, TagSerializer, UserLoginSerializer, UserRegistrationSerializer
from .models import Blog, Tags
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserRegistrationView(APIView):
  serializer_class = UserRegistrationSerializer
  permission_classes =(AllowAny,)

  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    valid = serializer.is_valid(raise_exception=True)

    if valid:
      serializer.save()
      status_code = status.HTTP_201_CREATED

      response = {
        'success': True,
        'statusCode':status_code,
        'message':'User successfully registered'
      }
      return Response(response, status =status.HTTP_200_OK)

class UserLoginView(APIView):
  serializer_class = UserLoginSerializer
  permission_classes = (AllowAny,)

  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    valid = serializer.is_valid(raise_exception=True)

    if valid:
      status_code = status.HTTP_200_OK
      response = {
        'success': True,
        'statusCode':status_code,
        'message':'User logged in successfully',
      }

      return Response(response, status =status.HTTP_200_OK)

# Create your views here.
