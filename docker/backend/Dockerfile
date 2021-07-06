FROM python:3.8-slim-buster

RUN apt update && apt install make -y

WORKDIR /backend

COPY ./backend/requirements.txt ./

RUN pip install -r requirements.txt && pip install django-cors-headers

COPY ./docker/ ./docker/
COPY ./backend/ ./
