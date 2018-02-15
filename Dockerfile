FROM python:3.6.3
LABEL version="1.1"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
#ENV SRV_PATH=/srv/www/html
#ENV PYTHONUNBUFFERED 1
#ENV DJANGO_ENV=prod
#ENV DOCKER_CONTAINER=1
#RUN apt-get update -q
    # apt-get dist-upgrade -y
#RUN mkdir -p $SRV_PATH && \
         #groupadd -g 350 -r -f medrec && \
         #useradd -r -m -u 350 -g 350 medrec
RUN apt-get install -y python3-dev libmysqlclient-dev

WORKDIR /medrec
RUN mkdir static logs
#RUN rm -r /srv/www/html/external
COPY . /medrec
#RUN pip install -r $SRV_PATH/requirements.txt
RUN pip install mysqlclient
RUN pip install -r requirements.txt
EXPOSE 8000
#CMD ["python3", "./medrec/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python3", "./medrec/manage.py", "runserver", "0.0.0.0:8000"]

