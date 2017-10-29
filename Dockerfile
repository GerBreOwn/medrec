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

RUN pip3 install --no-cache-dir -r $MEDREC_SRVPROJ/requirements.txt

## Install application requirements
#RUN mkdir /medrec
#WORKDIR /medrec
#COPY requirements.txt /medrec/ 
#COPY entrypoint.sh /medrec/
#RUN  pip3 install --no-cache-dir -r ./requirements.txt
#COPY  . /medrec/
## ENV DJANGO_ENV=prod
## Create django user, will own the Django app
#RUN adduser --no-create-home --disabled-login --group --system django
#RUN chown -R django:django /medrec/

EXPOSE 8000

## Execute start script
#ENTRYPOINT ["./entrypoint.sh"]

WORKDIR $MEDREC_SRVPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
