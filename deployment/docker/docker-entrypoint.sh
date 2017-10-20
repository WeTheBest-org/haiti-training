#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python /home/web/django_project/manage.py migrate

# Start server
echo "Starting server"
python /home/web/django_project/manage.py runserver 0.0.0.0:8080
