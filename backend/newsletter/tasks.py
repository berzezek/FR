from __future__ import absolute_import, unicode_literals
from celery import shared_task

import redis

import json
import requests

from .models import NewsletterStatistic

# redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, password=settings.REDIS_PASSWORD)
redis_instance = redis.Redis(host='redis', port=6379, db=0)

def create_log(list, newsletter_statistic_id, title, appoint):
    if len(list) > 0:
        count = 1
        file = open(f'logs/{newsletter_statistic_id}-{appoint}.txt', 'w')
        file.write(f'{title}\n')
        file.write(f'| # | Код | Номер телефона |\n')
        for i in list:
            file.write(f'| {count} | {i[ "phone_prefix" ]} | {i[ "phone_number" ]} |\n')
            count += 1
        file.write(f'-----------\nВсего: {count - 1}')
        file.close()


def send_to_test_server(url, data, newsletter_statistic_id):
    print(data)
    url += str(data[ 'newsletter' ])
    customer_received_list = [ ]
    customer_unreceived_list = [ ]
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

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()[ 'code' ] == 0:
            customer_received_list.append(customer)
        else:
            customer_unreceived_list.append(customer)
    redis_instance.hset(newsletter_statistic_id, 'customer_received_list', json.dumps(customer_received_list))

    # создаем логи
    create_log(customer_received_list, newsletter_statistic_id, 'Получили сообщение', 'received')
    create_log(customer_unreceived_list, newsletter_statistic_id, 'Не получили сообщение', 'unreceived')


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
