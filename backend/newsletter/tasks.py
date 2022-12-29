from __future__ import absolute_import, unicode_literals
import json

from celery import shared_task
import requests


def send_to_test_server(url, data):
    url += str(data[ 'id' ])
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
        print(response.text.encode('utf8'))


@shared_task
def send_delay_to_test_server(url, data):
    send_to_test_server(url, data)
