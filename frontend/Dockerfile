FROM node:16.3-buster-slim

RUN apt update

WORKDIR /frontend

COPY package*.json ./

RUN npm install && npm update chokidar

COPY . .

CMD npm start