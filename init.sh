#! /bin/bash

sudo unlink /etc/nginx/sites-enabled/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
