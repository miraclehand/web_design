# pull official base image
FROM python:3.9.6-slim-buster

LABEL maintainer="Yongeun Park <miraclehand@gmail.com>"

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

COPY ./requirements.txt /usr/src/web/requirements.txt

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/usr/src/web/entrypoint.sh"]
