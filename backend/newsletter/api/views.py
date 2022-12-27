import json

import redis
import requests
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import NewsletterSerializer, CustomerSerializer, NewsletterStatisticSerializer
from ..models import Newsletter, Customer, NewsletterStatistic


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def send_to_test_server(url, data):
    # payload = json.dumps(data)
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDMxNDc4MzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkJlcnplemVrIn0.sH0HctX2i1CvsI0E_PlnnHHJL9Ik1BXnsYGXgIuU9dI',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=data)

    if response.json()['code'] == 0:
        return True
    else:
        return False


redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class NewsletterStatisticViewSet(viewsets.ModelViewSet):
    queryset = NewsletterStatistic.objects.all()
    serializer_class = NewsletterStatisticSerializer

    # post
    def create(self, request, *args, **kwargs):
        data = request.data

        # get customer
        customer = Customer.objects.get(id=data['customer'])
        # get newsletter
        newsletter = Newsletter.objects.get(id=data['newsletter'])
        # print(newsletter.id, customer.get_full_phone_number(), newsletter.message, data["id"])

        items = {}
        count = 0
        for key in redis_instance.keys():
            items[key.decode('utf-8')] = redis_instance.get(key).decode('utf-8')
            count += 1
        print("items", items)
        # create statistic
        is_send = send_to_test_server(
            url=f'https://probe.fbrq.cloud/v1/send/{newsletter.id}',
            data=json.dumps({
                'id': newsletter.id,
                'phone': customer.phone_number,
                'text': newsletter.message,
            }),
        )

        statistic = NewsletterStatistic.objects.create(
            customer=customer,
            newsletter=newsletter,
            is_send=is_send
        )
        # serialize
        serializer = NewsletterStatisticSerializer(statistic)
        return Response(serializer.data)
