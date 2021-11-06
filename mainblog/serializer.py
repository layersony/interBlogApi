from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Tags, Blog
from django.contrib.auth.models import User

class TagSerial(serializers.RelatedField):
  """
  to_representation used to display the actual name of tag rather than it's Id
  """
  @classmethod
  def to_representation(cls, value):
    return value.tagname

  class Meta:
    model = Tags
    fields = '__all__'

class BlogSerializer(serializers.HyperlinkedModelSerializer):
  """
  HyperlinkedModelSerializer uses hyperlinked relationship rather than the primary key for multiple inputs
  """
  author = serializers.CharField(source='author.username', read_only=True)
  tags = TagSerial(read_only=True, many=True)

  class Meta:
    model = Blog
    fields = ('id', 'title', 'blogDetail', 'category', 'tags', 'author', 'created', 'updated',)

class TagSerializer(serializers.Serializer):
  class Meta:
    model = Tags
    fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
      """
      Create new user
      """
      auth_user = User.objects.create_user(**validated_data)
      return auth_user

class UserLoginSerializer(serializers.Serializer):
  
    username = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
      username = data["username"]
      password = data["password"]
      user = authenticate(username=username, password=password)

      if user is None:
        raise serializers.ValidationError("Invalid Login credentials")
      return user
