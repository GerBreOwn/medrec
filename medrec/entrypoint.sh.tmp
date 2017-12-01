#! /bin/bash

touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

echo Starting Gunicorn
exec gunicorn .medrec.wsgi:application \
        --name medrec \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --log-level=info \
        --log-file=/srv/logs/gunicorn.log \
        --access-logfile=/srv/logs/access.log \
        "$@"
