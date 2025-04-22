#!/bin/sh


python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput
gunicorn lesson_drf.wsgi --bind 0.0.0.0:8000 --workers 3 --threads 3 --reload