# REST API
from django.urls import path, include
# connects routes to views (controllers) - when i get a request here, execute views
from . import views
from .views import profile_list
app_name = "profiles_api"

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),     # this one views all 
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),     # just this one 
]