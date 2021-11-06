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
 
class BlogView(APIView):
  serializer_class = BlogSerializer

  def get(self, request, format=None):
    allblogs = Blog.objects.all()
    serializer = self.serializer_class(allblogs, many=True)
    response = {
      'success': True,
      'status_code': status.HTTP_200_OK,
      'message': 'Fetched Blogs',
      'blogs': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)

class BlogPostView(APIView):
  serializer_class = BlogSerializer
  permission_classes = (IsAuthenticated,)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save(author=request.user)
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):

  serializer_class = BlogSerializer
  permission_classes = (IsAuthenticated,)

  def getblog(self, pk):
    try:
      return Blog.objects.get(pk=pk)
    except: 
      res = {
        'message': f'Blog {pk} Not Found',
        'status': status.HTTP_204_NO_CONTENT
      }
      return Response(res)

  """
  Get single blog with primary key
  """
  def get(self, request, pk, format=None):
    blog = self.getblog(pk)
    try:
      serializers = self.serializer_class(blog)
      return Response(serializers.data)
    except:
      res = {
        'message': f'Blog {pk} Not Found',
        'status': status.HTTP_204_NO_CONTENT
      }
      return Response(res)


  """
  Update single blog with primary key
  """
  def put(self, request, pk, format=None):
    blog = self.getblog(pk)
    serializers = self.serializer_class(blog, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

  """
  delete single blog with primary key
  """
  def delete(self, request, pk, format=None):
    blog = self.getblog(pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class TagView(APIView):
  serializer_class = TagSerializer
  permission_classes = (IsAuthenticated,)

  def get(self, request, format=None):
    try:
      alltags = Tags.objects.all()
      serialTag = TagSerializer(alltags, many=True)
      response = {
        'success': True,
        'status_code': status.HTTP_200_OK,
        'message': 'Tags',
        'Tags': serialTag.data
      }
      return Response(response, status=status.HTTP_200_OK)
    except:
      
      return Response('Url is Via Post Append Slash at the End')

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
