import requests
from netflix.tools.movie_scraper import MovieScraper


class UpcomingPlugin(MovieScraper):
    def fetch_movies_from_source(self, url, genres):
        upcoming_movies = []
        for page in range(1, 14):
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for movie in data['results']:
                    print("Movie genre_ids:", movie['genre_ids'])
                    genre_names = [genres.get(genre_id, 'Unknown') for genre_id in movie['genre_ids']]
                    print("Genre names:", genre_names)
                    movie['category'] = ', '.join(genre_names)
                    upcoming_movies.append(movie)
            else:
                print(f'Failed to fetch data for page {page}')
        return upcoming_movies