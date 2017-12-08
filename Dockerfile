FROM python:3.6.3
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
ENV PYTHONUNBUFFERED 1
ENV MEDREC_SRC=/medrec/
ENV MEDREC_SRVHOME=/medrec/
ENV MEDREC_SRVPROJ=/medrec/
ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
RUN mkdir static logs
WORKDIR  $MEDREC_SRVPROJ
VOLUME ["$MEDREC_SRVHOME/media/", "$MEDREC_SRVHOME/logs/"]
COPY ./medrec/requirements.txt  $MEDREC_SRVPROJ
RUN pip install -r requirements.txt
COPY  ./medrec/* $MEDREC_SRVPROJ
RUN rm -rf srv
#VOLUME /var/lib/postgresql/data
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8000
CMD ["postgres"]
