# mtrpy

With [flask](http://flask.pocoo.org), [mtr](http://www.bitwizard.nl/mtr/).

Visit live demo here:

[mtr.io/static](http://mtr.io/static)

```
curl http://mtr.io
```

## INSTALLATION

```
sudo apt-get install nginx python python3-setuptools mtr-tiny \
git uwsgi uwsgi-plugin-python
sudo pip install virtualenv
cd /srv/www/mtrpy/application
virtualenv env
source env/bin/activate
pip install flask pbs
```

**/etc/uwsgi/apps-available/mtrpy.ini**

```
[uwsgi]
daemonize=/var/log/uwsgi/mtrpy.log
uwsgi-file=/srv/http/mtrpy/run.py
chdir=/srv/http/mtrpy/
pyhome=/srv/http/mtrpy/env
module=app
virtualenv=/srv/http/mtrpy/env
callable=app
plugin=python33
enable-threads=true
```

**/etc/nginx/sites-available/mtrpy**

```
limit_req_zone  $binary_remote_addr  zone=one:10m   rate=1r/s;
server {
    listen 80;
    server_name your.server.name.tld;

    location /static {
        alias /srv/www/mtrpy/static;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/app/mtrpy/socket;
    }

    location /mtrwindow {
        limit_req   zone=one  burst=5;
        include uwsgi_params;
        uwsgi_pass unix:/run/uwsgi/app/mtrpy/socket;
    }

    error 404 /404.html;
    error_page 500 502 503 504 /50x.html;

    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```

