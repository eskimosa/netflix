#!/bin/bash
# entrypoint.sh

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000
