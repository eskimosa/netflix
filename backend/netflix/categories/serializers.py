from rest_framework import serializers
from ..models import PopularMovie, TrendingMovie, UpcomingMovie, TopRatedMovie


class TopRatedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopRatedMovie
        fields = '__all__'


class PopularMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularMovie
        fields = '__all__'


class TrendingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingMovie
        fields = '__all__'


class UpcomingMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingMovie
        fields = '__all__'

