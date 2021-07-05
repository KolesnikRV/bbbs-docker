FROM python:3.8.5-alpine

RUN apt update && apt install make -y

WORKDIR /backend

COPY ./backend/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./backend/ ./