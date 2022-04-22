from rest_framework import serializers
from .models import Post
# serializers.ModelSerializer just tells django to convert sql objects to JSON data types
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # tell django which model to use
        fields = ('id', 'name', 'category', 'breed', 'description', 'city', 'state', 'img')  # tell django which fields to include
