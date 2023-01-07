FROM node:19-alpine

WORKDIR /frontend

COPY ./package*.json ./

EXPOSE 3000

RUN npm install

COPY . .
