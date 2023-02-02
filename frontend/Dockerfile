FROM node:19-alpine

WORKDIR /frontend

COPY ./package*.json ./

ENV HOST 0.0.0.0

EXPOSE 3000

RUN npm install

COPY . .

