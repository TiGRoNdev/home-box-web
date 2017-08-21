#! /bin/bash

git config --global user.name "TiGRoNdev"
git config --global user.email "tigron.dev@gmail.com"

sudo unlink /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-available/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/guincorn.d/default
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_app
sudo gunicorn -b 0.0.0.0:8000 ask/ask/wsgi:application
sudo /etc/init.d/mysql start
