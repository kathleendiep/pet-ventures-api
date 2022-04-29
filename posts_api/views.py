from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here - returns a web response from seralizer
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class UserViewSet(generics.ListCreateAPIView): 
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
