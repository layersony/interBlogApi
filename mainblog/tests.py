from django.test import TestCase
from django.urls import include, path, reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
import json


class UserTest(APITestCase, URLPatternsTestCase):
  """ Test module for User """

  urlpatterns = [
    path('', include('mainblog.urls')),
  ]
  def setUp(self):
    self.user1 = User.objects.create(username='testUser', password='test1234.')

  # def test_login(self):
  #   """ Test if a user can login """
  #   url = reverse('login')
  #   data = {
  #     'username':'testUser',
  #     'password':'test1234.'
  #   }
  #   response = self.client.post(url, data)
  #   print(response)
  #   response_Data = json.loads(response.content)
  #   print(response_Data)
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)
  #   self.assertEqual(response_Data['success'], True)
  #   self.assertTrue('access' in response_Data)

  def test_register(self):
    '''
    Test if a user can register
    '''
    url =reverse('register')
    data = {
      'username':'testUser',
      'password':'test1234.'
    }
    response = self.client.post(url,data)
    self.assertEqual(response.status_code,status.HTTP_201_CREATED)

  
