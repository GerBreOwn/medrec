FROM python:3.6

=======
# Add code
ADD ./medrec /srv/medrec

# Install application requirements
ADD ./config/requirements.txt /srv/medrec/
RUN pip3 install -r /srv/medrec/requirements.txt

# Add start script
ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
ADD ./config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/medrec

RUN mkdir /medrecapp
COPY . /medrecapp

# Execute start script
CMD ["./start.sh"]
