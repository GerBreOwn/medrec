FROM nginx:latest

LABEL version="1.0"

RUN apt-get update -q && \
         apt-get dist-upgrade -y && \
         apt-get install openssl && \
         apt-get clean && \
         apt-get autoclean

ENV SRV_PATH /srv/www/html

ARG PASSWORD=test         
         
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /srv/www/html && \
         chown nginx:nginx $SRV_PATH

RUN printf "user:$(openssl passwd -1 $PASSWORD)\n" >> $SRV_PATH/.htpasswd
         
 COPY nginx_main_site.conf /etc/nginx/conf.d/
 COPY test.txt /srv/www/html/
 
