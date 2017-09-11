FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN pip3 install pip-accel

RUN pip-accel install uwsgi

# Install application requirements
RUN mkdir /web
WORKDIR /web

COPY ./requirements.txt /web/
#COPY ./settings.py /web/

#RUN pip3 install -r ./requirements.txt
RUN pip-accel install -r ./requirements.txt
#ADD /web/* /web/
# COPY  ./web/* /web/
COPY  ./ /web/
ENV DJANGO_ENV=prod

# Add uWSGI config
COPY ./config/uwsgi.ini /etc/uwsgi/uwsgi.ini

# Add database check script
COPY ./config/database-check.py /web/config/database-check.py

# Create django user, will own the Django app
#RUN adduser --no-create-home --disabled-login --group --system django
#RUN chown -R django:django /web/

EXPOSE 8000

# Execute start script
CMD ["uwsgi","--ini", "./uwsgi.ini"]
