FROM python:3.8-alpine

RUN apk update

RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman