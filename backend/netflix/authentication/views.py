from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import UserMovieListSerializer, UserSerializer
from ..categories.serializers import MovieBaseSerializer
from ..models import UserMovieList, TopRatedMovie, TrendingMovie, UpcomingMovie, PopularMovie


class SignupView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Username is already in use."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"detail": "Email is already in use."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


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