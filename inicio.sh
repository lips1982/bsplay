#!/bin/bash

PUBLIC_IP=`wget http://ipecho.net/plain -O - -q ; echo`
echo "$PUBLIC_IP"

sed -i "s|REEMPLAZARPUBLICIP|${PUBLIC_IP}|g" botSpotifyV1/mainNeverInstall.py
sudo apt-get -y install screen

docker build -t display .


screen -S docker -d -m bash -c "docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display"
screen -S web -d -m bash -c "cd img/ && python3 -m http.server 8080"
