#!/bin/bash
echo $SERVICE_ACCOUNT_KEY | base64 -d > "deduce/$GOOGLE_APPLICATION_CREDENTIALS"
python deduce/manage.py makemigrations
python deduce/manage.py migrate
python deduce/manage.py collectstatic --no-input
gunicorn --chdir deduce --bind :$PORT deduce.wsgi:application