from rest_framework import serializers
from ..models import UserMovieList


class UserMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieList
        fields = '__all__'