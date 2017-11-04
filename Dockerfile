FROM python:3.6.3

MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>

ENV PYTHONUNBUFFERED 1
ENV MEDREC_SRC=medrec
ENV MEDREC_SRVHOME=/srv
ENV MEDREC_SRVPROJ=/srv/medrec

RUN mkdir static logs
WORKDIR  $MEDREC_SRVHOME

VOLUME ["$MEDREC_SRVHOME/media/", "$MEDREC_SRVHOME/logs/"]

COPY $MEDREC_SRC $MEDREC_SRVPROJ

RUN pip3 install -r $MEDREC_SRVPROJ/requirements.txt

EXPOSE 8000

## Execute start script
#ENTRYPOINT ["./entrypoint.sh"]

WORKDIR $MEDREC_SRVPROJ

COPY ./medrec/docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
