#!/bin/sh

# run.sh - to run a flaskdb docker container if it stop
# Copyright (C) 2024 Yasuhiro Hayashi

################################################################################

PROJECT_NAME="maps-flaskdb"

################################################################################

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker start $CONTAINER_ID; wait
fi
