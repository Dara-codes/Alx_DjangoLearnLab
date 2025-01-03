from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token, serializers.CharField(), Token.objects.create, get_user_model().objects.create_user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

