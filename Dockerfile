FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD /config/requirements.txt /config/

# Install application requirements
ADD ./src/ /src/

RUN pip3 install -r /config/requirements.txt

WORKDIR /src

# Add start script
ADD ./src/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
#ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/

# Execute start script
#CMD ["./start.sh"]
