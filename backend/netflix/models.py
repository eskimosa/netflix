from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    poster_path = models.URLField(max_length=500)
    category = models.CharField(max_length=255)
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title
