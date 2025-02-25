from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from netflix.categories.serializers import PopularMovieSerializer, TopRatedMovieSerializer, TrendingMovieSerializer, \
    UpcomingMovieSerializer
from netflix.models import PopularMovie, TopRatedMovie, TrendingMovie, UpcomingMovie


class PopularViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PopularMovie.objects.all()
    serializer_class = PopularMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class TopRatedViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = TopRatedMovie.objects.all()
    serializer_class = TopRatedMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class TrendingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = TrendingMovie.objects.all()
    serializer_class = TrendingMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']


class UpcomingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UpcomingMovie.objects.all()
    serializer_class = UpcomingMovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']
