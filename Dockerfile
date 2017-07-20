FROM python:3.6

# Install application requirements
#ADD ./webapp/requirements.txt /srv/
ADD ./webapp/ /srv/
RUN pip3 install -r /srv/requirements.txt

# Add start script
ADD ./webapp/start.sh /

# Add uWSGI config
ADD ./webapp/config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
ADD ./webapp/config/database-check.py /srv/config/database-check.py

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/

# Execute start script
CMD ["./start.sh"]
