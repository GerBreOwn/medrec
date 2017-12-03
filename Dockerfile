FROM python:3.6.3
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
ENV PYTHONUNBUFFERED 1
ENV MEDREC_SRC=medrec-top
ENV MEDREC_SRVHOME=/medrec/
ENV MEDREC_SRVPROJ=/medrec/
ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
RUN mkdir static logs
WORKDIR  $MEDREC_SRVPROJ
VOLUME ["$MEDREC_SRVHOME/media/", "$MEDREC_SRVHOME/logs/"]
COPY ./medrec/requirements.txt  $MEDREC_SRVPROJ
RUN pip install -r requirements.txt
COPY * $MEDREC_SRVPROJ
EXPOSE 80 8000 5432
#ENTRYPOINT ["gunicorn", "wsgi:application"]
VOLUME /var/lib/postgresql/data
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]
