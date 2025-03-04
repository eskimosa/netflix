from django.contrib import admin
from .models import TopRatedMovie, PopularMovie, TrendingMovie, UpcomingMovie, UserMovieList

admin.site.register(TopRatedMovie)
admin.site.register(PopularMovie)
admin.site.register(TrendingMovie)
admin.site.register(UpcomingMovie)
admin.site.register(UserMovieList)
