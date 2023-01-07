FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

#RUN apk add --update --no-cache postgresql-client jpeg-dev

COPY . .

