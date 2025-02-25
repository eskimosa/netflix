from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import UserMovieListSerializer, UserRegistrationSerializer
from ..categories.serializers import MovieBaseSerializer
from ..models import UserMovieList, TopRatedMovie, TrendingMovie, UpcomingMovie, PopularMovie

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            res = Response()

            res.data = {'success': True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            res.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            return res

        except:
            return Response({'success': False})


class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data

            access_token = tokens['access']

            res = Response()

            res.data = {'refreshed': True}

            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )

            return res
        except:
            return Response({'refreshed': False})


@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {'success': True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('refresh_token', path='/', samesite='None')
        return res
    except:
        return Response({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class UserMovieListViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
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