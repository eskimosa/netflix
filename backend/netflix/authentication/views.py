from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import UserMovieListSerializer
from ..categories.serializers import MovieBaseSerializer
from ..models import UserMovieList, TopRatedMovie, TrendingMovie, UpcomingMovie, PopularMovie


class UserMovieListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserMovieListSerializer

    def get_queryset(self):
        return UserMovieList.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_movie(self, request, pk=None):
        movie_id = request.data.get('movie_id')
        movie_type = request.data.get('movie_type')
        user = request.user

        if movie_type not in ['TopRatedMovie', 'PopularMovie', 'TrendingMovie']:
            return Response({'status': 'Invalid movie type'}, status=400)

        user_movie, created = UserMovieList.objects.get_or_create(
            user=user, movie_id=movie_id, movie_type=movie_type
        )

        if created:
            return Response({'status': 'Movie added to your list'}, status=201)
        else:
            return Response({'status': 'Movie already in your list'}, status=200)

    @action(detail=True, methods=['delete'])
    def remove_movie(self, request, pk=None):
        movie_id = request.data.get['movie_id']
        movie_type = request.data.get['movie_type']
        user = request.user

        try:
            user_movie = UserMovieList.objects.get(user=user, movie_id=movie_id, movie_type=movie_type)
            user_movie.delete()
            return Response({'status': 'Movie removed from your list'}, status=204)
        except UserMovieList.DoesNotExist:
            return Response({'status': 'Movie not found in your list'}, status=404)

    @action(detail=False, methods=['get'])
    def my_movies(self, request):
        user = request.user
        movie_list = UserMovieList.objects.filter(user=user)

        movies = []
        for entry in movie_list:
            movie = None
            if entry.movie_type == 'TopRatedMovie':
                movie = TopRatedMovie.objects.get(tmdb_id=entry.movie_id)
            elif entry.movie_type == 'PopularMovie':
                movie = PopularMovie.objects.get(tmdb_id=entry.movie_id)
            elif entry.movie_type == 'TrendingMovie':
                movie = TrendingMovie.objects.get(tmdb_id=entry.movie_id)
            elif entry.movie_type == 'UpcomingMovie':
                movie = UpcomingMovie.objects.get(tmdb_id=entry.movie_id)

            if movie:
                movies.append(movie)

        serializer = MovieBaseSerializer(movies, many=True)
        return Response(serializer.data)