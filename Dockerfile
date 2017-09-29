FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN pip3 install pip-accel
#RUN pip-accel install uwsgi
#RUN pip-accel install wsgi

# Install application requirements
RUN mkdir /medrec
WORKDIR /medrec

COPY ./requirements.txt /medrec/
RUN pip-accel install -r ./requirements.txt

COPY  . /medrec/


ENV DJANGO_ENV=prod

# Add uWSGI config
#COPY ./config/uwsgi.ini /etc/uwsgi/uwsgi.ini

# Add database check script
COPY ./medrec/config/database-check.py /medrec/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /medrec/

#EXPOSE 8000

# Execute start script
#CMD ["uwsgi", "--ini", "./uwsgi.ini"]
