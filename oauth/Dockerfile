FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /oauth

COPY . .

EXPOSE 8001

CMD ['python3', 'manage.py', 'runserver', '8001']
