from django.shortcuts import render
from tarsier.tarsierapi.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group #This is stuff for testing!
from rest_framework import viewsets

# Create your views here.

#This is stuff for testing starts here!

class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#This is stuff for testing ends here!