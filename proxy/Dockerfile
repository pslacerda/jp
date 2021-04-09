FROM nginx

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install nginx-full

COPY nginx.conf /etc/nginx/conf.d/default.conf
