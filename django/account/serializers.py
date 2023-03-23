from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo', 'date_of_birth']

        
class AccountPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo']

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']