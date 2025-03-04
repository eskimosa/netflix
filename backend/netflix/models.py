from django.db import models
from django.contrib.auth.models import User


class MovieBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    poster_path = models.URLField(max_length=500)
    category = models.CharField(max_length=255)
    tmdb_id = models.IntegerField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class TopRatedMovie(MovieBase):
    pass


class PopularMovie(MovieBase):
    pass


class TrendingMovie(MovieBase):
    pass


class UpcomingMovie(MovieBase):
    pass


class UserMovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()  # Store the movie's unique tmdb_id
    movie_type = models.CharField(max_length=255)  # Specify the movie type ('TopRatedMovie', etc.)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    poster_path = models.URLField(max_length=500)
    category = models.CharField(max_length=255)

    class Meta:
        unique_together = ('user', 'movie_id', 'movie_type')  # Prevent the same movie from being added twice by the
        # same user

    def __str__(self):
        return f'{self.user.username} - {self.movie_type} - {self.movie_id}'
