from django.db import models


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
