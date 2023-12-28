FROM python:3.9.16
LABEL maintainer="freemjstudio <mjwoo001@gmail.com>"
RUN apt-get -y update
RUN apt-get -y install vim 

RUN mkdir /srv/dev-server 
ADD srv /srv/dev-server

WORKDIR /srv/dev-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

