FROM python:3.6.3
LABEL version="1.0"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
#ENV SRV_PATH=/srv/www/html
#ENV PYTHONUNBUFFERED 1
#ENV DJANGO_ENV=prod
#ENV DOCKER_CONTAINER=1
#RUN apt-get update -q
    # apt-get dist-upgrade -y
RUN mkdir static logs
RUN rm -rf external
#RUN mkdir -p $SRV_PATH && \
         #groupadd -g 350 -r -f medrec && \
         #useradd -r -m -u 350 -g 350 medrec

# COPY ./medrec/manage.py  $SRV_PATH/manage.py/
# COPY ./medrec/requirements.txt  $SRV_PATH/
COPY . /srv/www/html
WORKDIR /srv/www/html
#RUN pip install -r $SRV_PATH/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
#VOLUME /var/lib/postgresql/data
#USER medrec
# ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]

