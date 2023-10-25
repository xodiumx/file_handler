#!/bin/bash

sleep 15

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic \
    --noinput

python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

gunicorn file_handler.wsgi:application --bind 0:8000

