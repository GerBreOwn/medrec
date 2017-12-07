#! /bin/bash
set -e

touch /logs/gunicorn.log
touch /logs/access.log

echo Starting Gunicorn
exec gunicorn wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 1 \

        "$@"
