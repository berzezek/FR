from __future__ import absolute_import, unicode_literals
import json

from celery import shared_task
import requests

import redis
from django.conf import settings

from .models import NewsletterStatistic

redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def send_to_test_server(url, data):
    url += str(data[ 'id' ])
    customer_send = [ ]
    for i in data[ 'customers' ]:
        payload = json.dumps({
            'id': data[ 'id' ],
            'phone': i[ 'phone_number' ],
            'text': data[ 'message' ],
        })
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                             '.eyJleHAiOjE3MDMxNDc4MzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkJlcnplemVrIn0'
                             '.sH0HctX2i1CvsI0E_PlnnHHJL9Ik1BXnsYGXgIuU9dI',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            customer_send.append(i[ 'id' ])
    redis_instance.set(str(data[ 'id' ]), json.dumps([ 'customer_send', json.dumps(customer_send) ]))


def update_customer_send(data):
    newsletter = NewsletterStatistic.objects.get(id=data[ 'newsletter' ])
    customer_send = [ ]
    for key in redis_instance.keys(str(data[ 'newsletter' ])):
        customer_send.append(redis_instance.get(key))
    customer_send = list(set(customer_send))
    newsletter.customer_send = customer_send
    newsletter.save()


@shared_task
def send_newsletter_task(url, data):
    send_to_test_server(url, data)


@shared_task
def update_customer_send_task(data):
    update_customer_send(data)
