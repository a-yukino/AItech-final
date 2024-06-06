#!/bin/sh

# deploy.sh - to build the flaskdb docker image
# Copyright (C) 2024 Yasuhiro Hayashi

################################################################################

USERNAME=`whoami`                     # a command to obtain your account name
HOST_PATH="/Users/$USERNAME"          # your home for building docker image
#HOST_PATH="/home/$USERNAME"          # your home for building docker image

PROJECT_NAME="maps-flaskdb"           # your project name
PROJECT_TAG="0.1"                     # latest or specific version of docker image
OUTER_PORT_FLASK=10003                # your network port to access docker containers
OUTER_PORT_POSTGRES=15003             # your network port to access docker containers

PROJECT_IPADDR="172.16.0.0/16"        # ip address for connecting docker containers
PROJECT_NETWORK="flaskdb-net"         # network name for connecting docker containers
CONTAINER_IPADDR="172.16.0.3"         # fix ip address for a docker container

################################################################################

chmod 644 Dockerfile
chmod 644 *.sh
chmod 755 deploy
chmod 755 flaskdb
chmod 644 flaskdb/*.py
chmod 644 flaskdb/*.ddl
chmod 644 flaskdb/flaskdb/*.py
chmod 755 flaskdb/flaskdb/static
chmod 755 flaskdb/flaskdb/static/css
chmod 644 flaskdb/flaskdb/static/css/*.css
chmod 755 flaskdb/flaskdb/static/js
chmod 644 flaskdb/flaskdb/static/js/*.js
chmod 755 flaskdb/flaskdb/templates
chmod 644 flaskdb/flaskdb/templates/*.html

rm deploy/flaskdb.tar.gz
tar cfvz deploy/flaskdb.tar.gz --exclude __pycache__ --exclude ".DS_Store" flaskdb

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker stop $CONTAINER_ID; wait
    docker rm $CONTAINER_ID; wait
fi

IMAGE_ID=`docker images | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 3`
if [ "$IMAGE_ID" != "" ]; then
    docker rmi $IMAGE_ID; wait
fi

NETWORK_ID=`docker network ls | grep $PROJECT_NETWORK | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$NETWORK_ID" != "" ]; then
    docker network rm $NETWORK_ID; wait
fi

docker builder prune -a
docker build -t $PROJECT_NAME:$PROJECT_TAG .
docker network create --subnet=$PROJECT_IPADDR $PROJECT_NETWORK

# select the statement below
docker run -it --name $PROJECT_NAME -p $OUTER_PORT_FLASK:8080 -p $OUTER_PORT_POSTGRES:5432 -v $HOST_PATH/$PROJECT_NAME/flaskdb:/flaskdb --network $PROJECT_NETWORK --ip $CONTAINER_IPADDR $PROJECT_NAME:$PROJECT_TAG # for unix, macos
#docker run -it --name $PROJECT_NAME -p $OUTER_PORT_FLASK:8080 -p $OUTER_PORT_POSTGRES:5432 -v c:\\$PROJECT_NAME\\flaskdb:/flaskdb --network $PROJECT_NETWORK --ip $CONTAINER_IPADDR $PROJECT_NAME:$PROJECT_TAG # for Windows
