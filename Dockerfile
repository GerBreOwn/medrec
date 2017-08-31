FROM python:3.6
ENV PYTHONUNBUFFERED 1

#RUN mkdir /config
#ADD /config/requirements.txt /config/

# Install application requirements
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/



# Add start script
#ADD . /src/
#ADD ./src/start.sh /

# Add uWSGI config
#ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Add database check script
#ADD ./config/database-check.py /src/config/database-check.py

# Create django user, will own the Django app
#RUN adduser --no-create-home --disabled-login --group --system django
#RUN chown -R django:django /src/

# Execute start script
#CMD ["./start.sh"]
