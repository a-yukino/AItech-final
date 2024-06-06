#!/bin/sh

# psql.sh - connects to PostgreSQL where a flaskdb docker container
# (C) Yasuhiro Hayashi

################################################################################

PROJECT_NAME="maps-flaskdb"

################################################################################

CONTAINER_ID=`docker ps -a | grep $PROJECT_NAME | sed -e 's/\ \ */\ /g' | cut -d " " -f 1`
if [ "$CONTAINER_ID" != "" ]; then
    docker start $CONTAINER_ID; wait
fi

if [ $# -ne 1 ]; then
    docker exec -it $CONTAINER_ID bash -c "su postgres -c \"psql $PROJECT_NAME\""
else
    docker exec -it $CONTAINER_ID bash -c "su postgres -c \"psql $1\""
fi
