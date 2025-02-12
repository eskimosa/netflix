from ..models import Movie
from .fetch_data import fetch_top_250_movies


def save_movies_to_db():
    top_movies = fetch_top_250_movies()
    for movie in top_movies:
        genre_names = movie['category']
        Movie.objects.update_or_create(
            tmdb_id=movie['id'],
            defaults={
                'title': movie['title'],
                'description': movie['overview'],
                'release_date': movie['release_date'],
                'rating': movie['vote_average'],
                'poster_path': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                'category': genre_names,
            }
        )
