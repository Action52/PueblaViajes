from .models import Viaje, Profile
from django.contrib.auth.models import User
from rest_framework import serializers

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ('title', 'description', 'start_date', 'end_date', 'price', 'imageBase64', 'contact_number')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'nation', 'trips')
