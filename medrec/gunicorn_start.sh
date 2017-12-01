#!/bin/bash

NAME="gerald"
DIR=medrec
USER=gsbmedrec
GROUP=gsbmedrec
WORKERS=3
BIND=unix:/usr/local/bin/gunicorn/gunicorn.sock
DJANGO_SETTINGS_MODULE=medrec.settings
DJANGO_WSGI_MODULE=medrec.wsgi
LOG_LEVEL=error

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-
