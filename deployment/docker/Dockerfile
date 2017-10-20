FROM python:2.7

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl

RUN apt-get -y update
RUN apt-get -y install \
    python-gdal \
    python-geoip \
    npm \
    nodejs \
    rpl

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apt-get -y install postgresql-client

ADD wait-for-postgis.sh /wait-for-postgis.sh
RUN chmod 0755 /wait-for-postgis.sh

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 0755 /docker-entrypoint.sh

EXPOSE 8080

WORKDIR /home/web/django_project

