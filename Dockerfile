FROM python:3.6.3
LABEL version="1.0"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
ENV SRV_PATH=/srv/www/html
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
#RUN apt-get update -q
    # apt-get dist-upgrade -y
RUN mkdir static logs
EXPOSE 8000
RUN mkdir -p $SRV_PATH && \
         groupadd -g 350 -r -f medrec && \
         useradd -r -m -u 350 -g 350 medrec
WORKDIR $SRV_PATH
# COPY ./medrec/manage.py  $SRV_PATH/manage.py/
# COPY ./medrec/requirements.txt  $SRV_PATH/
COPY . /$SRV_PATH/
RUN pip install -r $SRV_PATH/requirements.txt
#VOLUME $SRV_PATH/external
VOLUME /var/lib/postgresql/data
USER medrec
# ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "-m", "http.server"]

