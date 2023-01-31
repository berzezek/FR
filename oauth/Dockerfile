FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /oauth

COPY . /oauth

RUN pip install --no-cache-dir -r oauth.requirements.txt

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
