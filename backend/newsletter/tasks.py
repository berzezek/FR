from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging

import redis

import json
import requests

from .models import NewsletterStatistic

redis_instance = redis.Redis(host='redis', port=6379, db=0)

logger = logging.getLogger(__name__)


def send_to_test_server(url, data, newsletter_statistic_id):
    url += str(data[ 'newsletter' ])
    customer_received_list = [ ]
    customer_unreceived_list = [ ]
    logger.info(f'starting logs newsletter {newsletter_statistic_id}\n------------------\n')
    for customer in data[ 'customers' ]:
        payload = json.dumps({
            'id': data[ 'newsletter' ],
            'phone': customer[ 'phone_number' ],
            'text': data[ 'message' ],
        })
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
                             '.eyJleHAiOjE3MDMxNDc4MzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkJlcnplemVrIn0'
                             '.sH0HctX2i1CvsI0E_PlnnHHJL9Ik1BXnsYGXgIuU9dI',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            if response.json()[ 'code' ] == 0:
                customer_received_list.append(customer)
                logger.info(f'Customer {customer} received')
            else:
                customer_unreceived_list.append(customer)
                logger.warning(f'Customer {customer} unreceived')
        except Exception as e:
            logger.error(e)
            customer_unreceived_list.append(customer)

        redis_instance.hset(newsletter_statistic_id, 'customer_received_list', json.dumps(customer_received_list))
    logger.info(f'------------------\nnewsletter {newsletter_statistic_id} end sending logs\n')


def update_customer_received_list(newsletter_statistic_id):
    customer_received_str = redis_instance.hget(newsletter_statistic_id, 'customer_received_list').decode()
    customer_received_list = json.loads(customer_received_str)
    if len(customer_received_list) > 0:
        ns = NewsletterStatistic.objects.get(id=newsletter_statistic_id)
        for customer in customer_received_list:
            ns.customer.add(customer[ 'id' ])


@shared_task
def send_newsletter_task(url, data, newsletter_statistic_id):
    send_to_test_server(url, data, newsletter_statistic_id)
    update_customer_received_list(newsletter_statistic_id)
