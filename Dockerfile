FROM python:3.6.3
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
ENV PYTHONUNBUFFERED 1
ENV MEDREC_SRC=medrec
ENV MEDREC_SRVHOME=/srv
ENV MEDREC_SRVPROJ=/srv/medrec
RUN mkdir static logs
WORKDIR  $MEDREC_SRVPROJ
VOLUME ["$MEDREC_SRVHOME/media/", "$MEDREC_SRVHOME/logs/"]
COPY ./medrec/requirements.txt  $MEDREC_SRVPROJ
RUN pip3 install -r requirements.txt
COPY ./medrec/ $MEDREC_SRVPROJ
#COPY ./entrypoint.sh /
EXPOSE 8000:8000
ENTRYPOINT ["/entrypoint.sh"]
