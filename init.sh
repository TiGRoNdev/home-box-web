#! /bin/bash

sudo unlink /etc/nginx/sites-enabled/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/guincorn.d/
sudo /etc/init.d/gunicorn restart
sudo gunicorn hello:wsgi_app
sudo /etc/init.d/mysql start
