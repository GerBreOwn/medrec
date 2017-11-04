FROM python:3.6.3 

MAINTAINER Gerald S. Brown <gbrown@gerbreown.com> 

ENV PYTHONUNBUFFERED 1 
ENV MEDREC_SRC=medrec 
ENV MEDREC_SRVHOME=/srv 
ENV MEDREC_SRVPROJ=/srv/medrec 

RUN mkdir static logs #7

WORKDIR  $MEDREC_SRVPROJ #8

VOLUME ["$MEDREC_SRVHOME/media/", "$MEDREC_SRVHOME/logs/"] #9

#COPY $MEDREC_SRC $MEDREC_SRVPROJ #10
COPY . $MEDREC_SRVPROJ

RUN pip3 install -r $MEDREC_SRVPROJ/requirements.txt #11

EXPOSE 8000 #12

WORKDIR $MEDREC_SRVPROJ #13

COPY ./medrec/docker-entrypoint.sh /  #14

ENTRYPOINT ["/docker-entrypoint.sh"] #15
