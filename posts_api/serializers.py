from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
# serializers.ModelSerializer just tells django to convert sql objects to JSON data types
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # tell django which model to use
        fields = ('id', 'name', 'category', 'breed', 'info', 'city', 'state', 'image')  # tell django which fields to include

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']