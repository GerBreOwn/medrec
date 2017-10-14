#!/bin/bash

# Start Gunicorn processes
echo "Starting Gunicorn"

exec gunicorn medrec.wsgi:application \
    --chdir=/medrec/
    --bind 0.0.0.0:8000 \
    --workers 2
