FROM python:3.6.3
LABEL version="1.1"
MAINTAINER Gerald S. Brown <gbrown@gerbreown.com>
WORKDIR /medrec
RUN mkdir static logs
COPY . /medrec
RUN pip install -r requirements.txt
COPY my.cnf /etc/mysql/conf.d/
RUN apt-get update && apt-get install nano
EXPOSE 8001
CMD ["python3", "./medrec/manage.py", "runserver", "0.0.0.0:8001"]

