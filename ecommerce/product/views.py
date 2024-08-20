from django.shortcuts import get_object_or_404 
from django.contrib.auth.models import User, Group 

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response 
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle 
from rest_framework import status  

from . models import Category 
from . serializers import CategorySerializer 
from . permissions import IsManager


# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    """
    View to list all categories or create a new category.

    - GET: Any user (authenticated or anonymous) can view the list of categories.
    - POST, PATCH, DELETE: Only authenticated users who are either managers or superusers can create, update, or delete categories.
    """
    throttle_classes = [AnonRateThrottle, UserRateThrottle] # Applying rate limiting to requests
    queryset = Category.objects.all() # Define queryset to use
    serializer_class = CategorySerializer # Specifiy serializer for Category object

    def get_permissions(self):
        """
        Override the default method to customize permissions based on the request method.
        - GET: Allow all users.
        - POST, PATCH, DELETE: Restrict to authenticated managers or superusers.
        """
        permission_classes = []
        if self.request.method != "GET": # If request method is not GET
            # Requires user to be authenticated and either manager or superuser
            permission_classes = [IsAuthenticated, IsManager | IsAdminUser]
    
        return [permission() for permission in permission_classes] # Instantiate permissions
    

class ProductView(generics.ListCreateAPIView):
    pass 