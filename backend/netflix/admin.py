from django.contrib import admin
from .models import TopRatedMovie, PopularMovie, TrendingMovie, UpcomingMovie

admin.site.register(TopRatedMovie)
admin.site.register(PopularMovie)
admin.site.register(TrendingMovie)
admin.site.register(UpcomingMovie)
