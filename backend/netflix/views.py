from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from netflix.models import Movie
from netflix.serializers import MovieSerializer
from .tools.fetch_data import fetch_top_250_movies

API_KEY_TMDB = '1f2af6b2d576ca12e9918b023952b2ff'


'''class MovieApiFetchViewSet(viewsets.ViewSet):
def list(self, request, *args, **kwargs):
    # Fetch data directly from the API
    top_movies = fetch_top_250_movies()
    return Response(top_movies)'''


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'rating']



