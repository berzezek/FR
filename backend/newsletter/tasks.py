from __future__ import absolute_import, unicode_literals
import json

from celery import shared_task
import requests

import redis
from django.conf import settings
from .models import NewsletterStatistic

redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, password=settings.REDIS_PASSWORD)


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
    redis_instance.hset(str(data[ 'id' ]), 'customer_send', json.dumps(customer_send))


def update_customer_send(newsletter_id, newsletter_statistic_id):
    redis_instance = redis.Redis(host='redis-19400.c299.asia-northeast1-1.gce.cloud.redislabs.com', port=19400, db=0,
                                 password='rdAyjWP6HjpE15dG7K8iMdnKzEC0fMnH')
    customer_send = redis_instance.hget(newsletter_id, 'customer_send').decode()[ 1:-1 ].split(',')
    ns = NewsletterStatistic.objects.get(id=newsletter_statistic_id)
    ns.customer_send.set(customer_send)


@shared_task
def send_newsletter_task(url, data, newsletter_statistic_id):
    send_to_test_server(url, data)
    update_customer_send(data[ 'id' ], newsletter_statistic_id)
