from rest_framework import serializers
from django.contrib.auth.models import User


from ..models import UserMovieList


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieList
        fields = '__all__'