
def save_movies_to_db(model, movies):
    for movie in movies:
        genre_names = movie['category']
        model.objects.update_or_create(
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

    return movies

'''def save_movies_to_db(model):
    top_movies = fetch_top_250_movies()
    for movie in top_movies:
        genre_names = movie['category']
        model.objects.update_or_create(
            tmdb_id=movie['id'],
            defaults={
                'title': movie['title'],
                'description': movie['overview'],
                'release_date': movie['release_date'],
                'rating': movie['vote_average'],
                'poster_path': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                'category': genre_names,
            }
        )'''


'''class SaveMovies:
    def save_movies_to_db(self, movies, serializer):
        serializer = serializer(data=movies)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        else:
        return serializer.errors, status.HTTP_400_BAD_REQUEST'''