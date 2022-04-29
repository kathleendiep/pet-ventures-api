from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here - returns a web response from seralizer
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ProfileSerializer # tell django what serializer to use
    # authentication_classes = [TokenAuthentication]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request,'', {"profiles": profiles})



# class UserViewSet(generics.ListCreateAPIView): 
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     # authentication_classes = [TokenAuthentication]