from django.core.management.base import BaseCommand
from netflix.tools.save_data import save_movies_to_db


class Command(BaseCommand):
    help = 'Fetch top 250 movies from TMDb API and save them to the database'

    def handle(self, *args, **kwargs):
        save_movies_to_db()
        self.stdout.write(self.style.SUCCESS('Successfully imported movies from TMDb'))

