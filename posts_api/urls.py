# REST API
from django.urls import path
# connects routes to views (controllers) - when i get a request here, execute views
from . import views

urlpatterns = [
# CHANGED the url for react
path('', views.PostList.as_view(), name='post_list'), # api/contacts will be routed to the ContactList view for handling
path('<int:pk>', views.PostDetail.as_view(), name='post_detail'), # api/contacts will be routed to the ContactDetail view for handling
]