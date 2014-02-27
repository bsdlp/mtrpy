FROM docku/uwsgi
MAINTAINER Jon Chen <docku@burrito.sh>

RUN /usr/bin/apt-get -y uwsgi-plugin-python3

ADD mtrpy.ini /etc/uwsgi/apps-enabled/mtrpy.ini

