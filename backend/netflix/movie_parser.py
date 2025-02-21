import os

from rest_framework.response import Response
from rest_framework.views import APIView

from netflix.categories.popular import PopularPlugin
from netflix.categories.top_rated import TopRatedPlugin
from netflix.categories.trending import TrendingPlugin
from netflix.categories.upcoming import UpcomingPlugin
from netflix.models import PopularMovie, TopRatedMovie, TrendingMovie, UpcomingMovie

API_KEY = os.environ.get('API_KEY_TMDB')

popular = 'https://api.themoviedb.org/3/movie/popular?api_key={key}&language=en-US&page=4'
trending = 'https://api.themoviedb.org/3/trending/movie/day?api_key={key}&language=en-US&page=4'
top_rated = 'https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=en-US&page=4'
upcoming = 'https://api.themoviedb.org/3/movie/upcoming?api_key={key}&language=en-US&page=4'


class MovieParserAPIView(APIView):
    def get(self, request):
        try:
            popular_plugin = PopularPlugin(url=popular.format(key=API_KEY), model=PopularMovie)
            popular_movies = popular_plugin.execute()

            trending_plugin = TrendingPlugin(url=trending.format(key=API_KEY), model=TrendingMovie)
            trending_movies = trending_plugin.execute()

            top_rated_plugin = TopRatedPlugin(url=top_rated.format(key=API_KEY), model=TopRatedMovie)
            top_rated_movies = top_rated_plugin.execute()

            upcoming_plugin = UpcomingPlugin(url=upcoming.format(key=API_KEY), model=UpcomingMovie)
            upcoming_movies = upcoming_plugin.execute()
            return Response({'popular': popular_movies, 'trending': trending_movies, 'upcoming': upcoming_movies,
                             'top_rated': top_rated_movies})
        except Exception as e:
            return Response({'error': str(e)})
