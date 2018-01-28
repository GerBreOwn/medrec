FROM python:3.6.3
LABEL version="1.0"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
ENV SRV_PATH=/srv/www/html
ENV PYTHONUNBUFFERED 1
ENV MEDREC_SRC=/medrec-top/medrec/
ENV MEDREC_SRVHOME=/medrec/
ENV MEDREC_SRVPROJ=/medrec/
ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
# RUN apt-get update -q && \
#         apt-get dist-upgrade -y
RUN mkdir static logs
EXPOSE 8000
RUN mkdir -p $SRV_PATH && \
         groupadd -g 350 -r -f medrec && \
         useradd -r -m -u 350 -g 350 medrec
COPY ./medrec/entrypoint.sh $SRV_PATH/
#COPY ./medrec/manage.py $SRV_PATH/
COPY manage.py $SRV_PATH/
COPY ./medrec/requirements.txt  $SRV_PATH/
RUN pip install -r $SRV_PATH/requirements.txt
USER medrec
# RUN chown -R medrec:medrec $SRV_PATH
WORKDIR $SRV_PATH
VOLUME $SRV_PATH/external
COPY ./*/* $SRV_PATH/
VOLUME /var/lib/postgresql/data

# ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "-m", "http.server"]

