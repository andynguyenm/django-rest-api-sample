from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketListSerializer, UserSerializer
from .models import BucketList
from rest_framework import permissions
from .permissions import IsOwner
from django.contrib.auth.models import User


# Create your views here.


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated,)  # ADD THIS LINE

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
