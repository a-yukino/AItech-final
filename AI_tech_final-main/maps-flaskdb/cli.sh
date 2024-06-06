#!/bin/sh

# cli.sh - provides a console to access the flaskdb docker image container
# Copyright (C) 2024 Yasuhiro Hayashi

################################################################################

PROJECT_NAME="maps-flaskdb"

################################################################################

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker start $CONTAINER_ID; wait
fi

docker exec -it -w /flaskdb $CONTAINER_ID bash
