from django.urls import path

from .movie_parser import MovieParserAPIView
from .movies.views import PopularViewSet, UpcomingViewSet, TrendingViewSet, TopRatedViewSet

# from .views import MovieViewSet

urlpatterns = [
    # path('movies/', MovieViewSet.as_view({'get': 'list'}), name='movies'),
    path('fetch_movies/', MovieParserAPIView.as_view(), name='fetch_movies_api'),
    path('list_popular/', PopularViewSet.as_view({'get': 'list'}), name='popular_movies_api'),
    path('list_upcoming/', UpcomingViewSet.as_view({'get': 'list'}), name='upcoming_movies_api'),
    path('list_trending/', TrendingViewSet.as_view({'get': 'list'}), name='trending_movies_api'),
    path('list_top_rated/', TopRatedViewSet.as_view({'get': 'list'}), name='top_rated_movies_api'),
    # path('get_movies/', MovieApiFetchViewSet.as_view({'get': 'list'}), name='get_movies'),
]