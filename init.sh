#! /bin/bash

git config --global user.name "TiGRoNdev"
git config --global user.email "tigron.dev@gmail.com"

sudo unlink /etc/nginx/sites-enabled/default
sudo unlink /etc/nginx/sites-available/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_app
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
#sudo /etc/init.d/mysql start
