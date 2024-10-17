from rest_framework import serializers

from companies.models import Company
from users.models import User
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Cериализация регистрации пользователя. (Модель User)
    """
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'phone', 'last_name', 'email', 'password', 'companies',]


class CurrentUserSerializer(serializers.ModelSerializer):
    """Отображение данных пользователя. (Модель User)"""
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone', 'companies',]



class UserSerializer(serializers.ModelSerializer):
    """Отображение данных списка пользователей. (Модель User)"""
    companies = serializers.StringRelatedField(many=True)
    class Meta:

        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'companies']
