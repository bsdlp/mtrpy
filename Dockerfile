FROM docku/uwsgi
MAINTAINER Jon Chen <docku@burrito.sh>

RUN /usr/bin/pacman -Syu --needed --noconfirm uwsgi-plugin-python

ADD mtrpy.ini /etc/uwsgi/apps-enabled/mtrpy.ini
