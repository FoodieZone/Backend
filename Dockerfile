FROM python:3.9.16
LABEL maintainer="freemjstudio <mjwoo001@gmail.com>"
RUN apt-get -y update

RUN python3 -m venv venv && . venv/bin/activate
RUN mkdir /srv/dev-server
ADD src /srv/dev-server
COPY requirements.txt /srv/dev-server/requirements.txt

WORKDIR /srv/dev-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
EXPOSE 8080
