import imghdr
from rest_framework import serializers
from .models import Profile, Dweet
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

# serializers.ModelSerializer just tells django to convert sql objects to JSON data types
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    follows = serializers.CharField()
    class Meta:
        model = Profile  # tell django which model to use
        fields = ('id', 'user', 'follows')  # tell django which fields to include

    def create_profile(self, validated_data):
        user_profile = Profile(
            user= validated_data['user'],
            follows= validated_data['follows']
        )
        return user_profile 
    
    def profile_list(self,validated_data): 
        profiles=validated_data('profiles')
        return profiles

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model = Dweet  # tell django which model to use
        fields = ('id', 'user', 'body', 'created_at', 'petname','category', 'breed', 'city', 'state', 'img',)  # tell django which fields to include

# how to make it follow others
    # @receiver(post_save, sender=User)
    # def create_profile(self, created, validated_data):
    #     if created: 
    #         user_profile = Profile(user=validated_data['user'])
    #         user_profile.save()
    #         user_profile.follows.add(instance.profile)
    #         user_profile.save()
