from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
# serializers.ModelSerializer just tells django to convert sql objects to JSON data types
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # tell django which model to use
        fields = ('id', 'name', 'category', 'breed', 'info', 'city', 'state', 'image')  # tell django which fields to include

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password': {
            'write_only':True,
            'required': True
        }}

    def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user
