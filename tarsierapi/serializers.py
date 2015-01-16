# This is the data representation of tarsierapi. It describes datamodels.

#TODO: Serializers.py should read classes from a config file. 

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class TarsierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('key', 'object')

class T2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('key', 'object')

