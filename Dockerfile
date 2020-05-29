# pull official base image
FROM python:3.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./etc/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# setup cronjob
COPY ./etc/cron/fetch-cron /etc/cron.d/fetch-cron
RUN chmod 0644 /etc/cron.d/fetch-cron
RUN crontab /etc/cron.d/fetch-cron

# copy project
COPY . /usr/src/app/

