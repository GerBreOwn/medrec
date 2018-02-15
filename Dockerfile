FROM python:3.6.3
LABEL version="1.1"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
WORKDIR /medrec
RUN mkdir static logs
COPY . /medrec
RUN pip install mysqlclient django-mysql
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "./medrec/manage.py", "runserver", "0.0.0.0:8000"]

