from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from netflix.categories.serializers import PopularMovieSerializer, TopRatedMovieSerializer, TrendingMovieSerializer, \
    UpcomingMovieSerializer
from netflix.models import PopularMovie, TopRatedMovie, TrendingMovie, UpcomingMovie


class PopularViewSet(viewsets.ModelViewSet):
    queryset = PopularMovie.objects.all()
    serializer_class = PopularMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class TopRatedViewSet(viewsets.ModelViewSet):
    queryset = TopRatedMovie.objects.all()
    serializer_class = TopRatedMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class TrendingViewSet(viewsets.ModelViewSet):
    queryset = TrendingMovie.objects.all()
    serializer_class = TrendingMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class UpcomingViewSet(viewsets.ModelViewSet):
    queryset = UpcomingMovie.objects.all()
    serializer_class = UpcomingMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']
