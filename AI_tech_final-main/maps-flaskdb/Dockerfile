# Dockerfile - to build the flaskdb docker image including PostgreSQL and a sample web app
# Copyright (C) 2024 Yasuhiro Hayashi

#FROM ubuntu:latest
FROM ubuntu:jammy
ENV DEBIAN_FRONTEND=noninteract

ENV PROJECT_NAME=maps-flaskdb

USER root
RUN apt -y update
RUN apt -y upgrade

RUN apt -y install locales
RUN locale-gen ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" LANGUAGE="ja_JP:ja" LC_ALL="ja_JP.UTF-8"

RUN apt -y install tzdata
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt -y install vim

RUN apt -y install python3
RUN apt -y install python3-pip

RUN echo "alias python='python3'" >> /root/.bashrc
RUN echo "alias pip='pip3'" >> /root/.bashrc
RUN ["/bin/bash", "-c", "source /root/.bashrc"]

#RUN apt -y install curl ca-certificates
#RUN install -d /usr/share/postgresql-common/pgdg
#RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
#RUN sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
#RUN apt -y update

RUN apt -y install libpq-dev
#RUN apt -y install postgresql-14
RUN apt -y install postgresql

ADD deploy/flaskdb.tar.gz /

COPY flaskdb/requirements.txt /flaskdb/

#RUN pip3 install --break-system-packages --upgrade pip
#RUN pip3 install --break-system-packages -r /flaskdb/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /flaskdb/requirements.txt

USER postgres
RUN cp /etc/postgresql/14/main/postgresql.conf /etc/postgresql/14/main/postgresql.conf.default
RUN sed -i -e "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/14/main/postgresql.conf
RUN sed -i -e "s/^#password_encryption = scram-sha-256/password_encryption = md5/g" /etc/postgresql/14/main/postgresql.conf
RUN cp /etc/postgresql/14/main/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf.default
RUN sed -i -e "s/^host    all             all             127.0.0.1\/32            scram-sha-256/host    all             all            0.0.0.0\/0                md5/g" /etc/postgresql/14/main/pg_hba.conf
RUN /etc/init.d/postgresql start && wait && /usr/bin/createdb -O postgres ${PROJECT_NAME} && wait && psql ${PROJECT_NAME} < /flaskdb/createdb.ddl

USER root
EXPOSE 5432
EXPOSE 8080
VOLUME  ["/flaskdb", "/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

ENV FLASK_APP /flaskdb/app.py
CMD /etc/init.d/postgresql restart && wait && /usr/local/bin/flask run -h 0.0.0.0 -p 8080 --debug --reload --debugger
