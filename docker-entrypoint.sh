#!/bin/bash
python deduce/manage.py makemigrations
python deduce/manage.py migrate
python deduce/manage.py collectstatic --no-input
gunicorn --chdir deduce --bind :8000 deduce.wsgi:application