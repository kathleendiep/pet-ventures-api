# REST API
from django.urls import path, include
# connects routes to views (controllers) - when i get a request here, execute views
from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),     # this one views all 
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),     # just this one 
    path('articles/', views.ArticleList.as_view(), name='article_list'),     # this one views all 
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),     # just this one 
    
]