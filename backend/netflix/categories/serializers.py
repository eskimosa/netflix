from rest_framework import serializers
from ..models import MovieBase, PopularMovie, TrendingMovie, UpcomingMovie, TopRatedMovie


class MovieBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieBase
        fields = '__all__'


class TopRatedMovieSerializer(MovieBaseSerializer):
    class Meta(MovieBaseSerializer.Meta):
        model = TopRatedMovie


class PopularMovieSerializer(MovieBaseSerializer):
    class Meta(MovieBaseSerializer.Meta):
        model = PopularMovie


class TrendingMovieSerializer(MovieBaseSerializer):
    class Meta(MovieBaseSerializer.Meta):
        model = TrendingMovie


class UpcomingMovieSerializer(MovieBaseSerializer):
    class Meta(MovieBaseSerializer.Meta):
        model = UpcomingMovie
