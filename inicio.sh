#!/bin/bash
clear
echo "INICIANDO"
sudo service docker stop

while getopts k: option
do 
    case "${option}"
        in
        k)SERVERNAME=${OPTARG};;

    esac
done
echo "KEY_ACCES : $SERVERNAME"

sed -i "s|SERVERNAME|${SERVERNAME}|g" daemon.json

sudo cp -f daemon.json /etc/docker/

sudo service docker start

PUBLIC_IP=`wget http://ipecho.net/plain -O - -q ; echo`
echo "$PUBLIC_IP"

sed -i "s|REEMPLAZARPUBLICIP|${PUBLIC_IP}|g" botSpotifyV1/mainNeverInstall.py
sudo apt-get -y install screen

docker build -t display .


screen -S docker -d -m bash -c "docker run -it --rm -v $PWD/img:/app/Almacenamiento/img display"
screen -S web -d -m bash -c "cd img/ && python3 -m http.server 8080"
