#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
printf %s "xD
" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server_name _;/a \        location /hbnb_static {\n' /etc/nginx/sites-available/default
sed -i '/hbnb_static {/a \                alias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
