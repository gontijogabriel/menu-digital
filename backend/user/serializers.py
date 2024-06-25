from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password
import re 


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['cpf'] = re.sub(r'\D', '', validated_data['cpf'])
        return super(UserSerializer, self).create(validated_data)