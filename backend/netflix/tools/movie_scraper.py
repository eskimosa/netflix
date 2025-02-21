import requests
import os
from abc import ABC, abstractmethod

from netflix.tools import save_data


class MovieScraper(ABC):
    def __init__(self, url, model):
        self.url = url
        self.model = model

    API_KEY = os.environ.get('API_KEY_TMDB')
    GENRES_URL = 'https://api.themoviedb.org/3/genre/movie/list'

    def fetch_genres(self):
        """
        Fetches genre mapping from TMDB and returns a dictionary with genre IDs as keys
        and genre names as values.
        """

        genres = {}
        response = requests.get(f'{self.GENRES_URL}?api_key={self.API_KEY}&language=en-US')
        if response.status_code == 200:
            data = response.json()
            for genre in data['genres']:
                genres[genre['id']] = genre['name']
        else:
            print('Failed to fetch genres')
        return genres

    def execute(self):
        # Fetch genres
        genres = self.fetch_genres()

        # Fetch movies from the API
        fetch_movies = self.fetch_movies_from_source(self.url, genres)

        # Save the movies to the db
        saved_movies = save_data.save_movies_to_db(self.model, fetch_movies)
        return saved_movies

    @abstractmethod
    def fetch_movies_from_source(self, urls, genres):
        pass


'''def fetch_genres():
    genres = {}
    response = requests.get(f'{GENRES_URL}?api_key={API_KEY}&language=en-US')
    if response.status_code == 200:
        data = response.json()
        for genre in data['genres']:
            genres[genre['id']] = genre['name']
    else:
        print('Failed to fetch genres')
    return genres


def fetch_top_250_movies():
    # import pdb; pdb.set_trace()

    top_movies = []
    genres = fetch_genres()
    for page in range(1, 14):
        url = f'{BASE_URL}?api_key={API_KEY}&language=en-US&page={page}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results']:
                print("Movie genre_ids:", movie['genre_ids'])
                genre_names = [genres.get(genre_id, 'Unknown') for genre_id in movie['genre_ids']]
                print("Genre names:", genre_names)
                movie['category'] = ', '.join(genre_names)
                top_movies.append(movie)
        else:
            print(f'Failed to fetch data for page {page}')
    return top_movies'''
