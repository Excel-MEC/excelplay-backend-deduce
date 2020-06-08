#!/bin/bash
echo $SERVICE_ACCOUNT_KEY | base64 -d > "deduce/$GOOGLE_APPLICATION_CREDENTIALS"
# python deduce/manage.py migrate
gunicorn --chdir deduce --bind :$PORT --workers=$WORKERS --threads=$THREADS --worker-class=gthread deduce.wsgi:application