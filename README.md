# mtrpy

With [flask](http://flask.pocoo.org), [pbs](https://github.com/amoffat/pbs), and [mtr](http://www.bitwizard.nl/mtr/).

Visit live demo here:

[mtr.io/static](http://mtr.io/static)

    curl http://mtr.io

## INSTALLATION

    sudo apt-get install nginx python python-distribute mtr-tiny git uwsgi uwsgi-plugin-python
    sudo pip install virtualenv
    cd /srv/www/mtrpy/application
    virtualenv env
    source env/bin/activate
    pip install flask pbs

**/etc/uwsgi/apps-available/mtrpy.ini**

    [uwsgi]
    plugins=python
    vhost=true
    socket=/tmp/mtrpy.sock

**/etc/nginx/sites-available/mtrpy**

    server {
        listen              80;
        server_name         your.server.name.tld;
        
        location /static {
            alias           /srv/www/mtrpy/static;
        }

        location / {
            include         uwsgi_params;
            uwsgi_pass      unix:/tmp/mtrpy.sock;
            uwsgi_param     UWSGI_PYHOME    /srv/www/mtrpy/application/env;
            uwsgi_param     UWSGI_CHDIR     /srv/ww/mtrpy/application;
            uwsgi_param     UWSGI_MODULE    application;
            uwsgi_param     UWSGI_CALLABLE  app;
        }

        error   404         /404.html;

        error_page  500 502 503 504 /50x.html;
        location = /50x.html {
            root            /usr/share/nginx/html;
        }
    }
