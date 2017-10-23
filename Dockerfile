FROM python:3.6.3

MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>

ENV PYTHONUNBUFFERED 1

# RUN pip3 install pip-accel

# Install application requirements
RUN mkdir /medrec
WORKDIR /medrec

COPY requirements.txt /medrec/
COPY start.sh /start.sh

RUN  pip3 install -r ./requirements.txt

COPY  . /medrec/

# ENV DJANGO_ENV=prod

# Create django user, will own the Django app
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /medrec/

EXPOSE 80:8000

# Execute start script
CMD ["/start.sh"]
