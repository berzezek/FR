import json

import redis
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from ..tasks import send_delay_to_test_server

from .serializers import NewsletterSerializer, CustomerSerializer, NewsletterStatisticSerializer, \
    CustomerStatisticSerializer
from ..models import Newsletter, Customer, NewsletterStatistic, CustomerStatistic


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def send_mess():
    print('send_mess')


class NewsletterStatisticViewSet(viewsets.ModelViewSet):
    queryset = NewsletterStatistic.objects.all()
    serializer_class = NewsletterStatisticSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     r = send_delay_to_test_server
    #     r.apply_async((
    #         f'https://probe.fbrq.cloud/v1/send/1',
    #         json.dumps({
    #             'id': 1,
    #             'phone': 123456789,
    #             'text': 'Hello world',
    #         })),
    #         countdown=10, expires=10
    #     )
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     redis_instance.publish('newsletter', json.dumps(serializer.data))
    #     return Response(serializer.data, status=201, headers=headers)

    # post
    def create(self, request, *args, **kwargs):
        # send newsletter

        # r = send_delay_to_test_server
        # r.apply_async((request.data,), countdown=1, expires=10)
        r = send_delay_to_test_server
        r.apply_async(('https://probe.fbrq.cloud/v1/send/', request.data), countdown=1, expires=10)

        # statistic = NewsletterStatistic.objects.create()
        # # serialize
        # serializer = NewsletterStatisticSerializer(statistic)
        # return Response(serializer.data)
        return Response({'status': 'ok'})


class CustomerStatisticViewSet(viewsets.ModelViewSet):
    queryset = CustomerStatistic.objects.all()
    serializer_class = CustomerStatisticSerializer
