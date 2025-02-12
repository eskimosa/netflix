import requests
import os

API_KEY = os.environ.get('API_KEY_TMDB')
BASE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
GENRES_URL = 'https://api.themoviedb.org/3/genre/movie/list'


def fetch_genres():
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
    return top_movies
