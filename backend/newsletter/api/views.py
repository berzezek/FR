from django.utils import timezone

import redis
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from ..tasks import send_newsletter_task, update_customer_send_task

from .serializers import NewsletterSerializer, CustomerSerializer, NewsletterStatisticSerializer, \
    NewsletterStatisticListSerializer
from ..models import Newsletter, Customer, NewsletterStatistic


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


class NewsletterStatisticViewSet(viewsets.ModelViewSet):
    queryset = NewsletterStatistic.objects.all()
    serializer_class = NewsletterStatisticSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NewsletterStatisticListSerializer(queryset, many=True)
        return Response(serializer.data)



    def create(self, request, *args, **kwargs):
        request.data[ 'customer_to_send' ] = [ ]
        for i in request.data[ 'customers' ]:
            request.data[ 'customer_to_send' ].append(i[ 'id' ])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # send_newsletter
        newsletter = Newsletter.objects.get(id=request.data[ 'newsletter' ])
        start_launch_date = newsletter.start_launch_date
        end_launch_date = newsletter.end_launch_date
        countdown = (start_launch_date - timezone.now()).total_seconds()
        expires = (end_launch_date - timezone.now()).total_seconds()
        if countdown < 0:
            countdown = 0
        if expires < 0:
            return Response({'error': 'End launch date is in the past'})

        task_1 = send_newsletter_task
        task_1.apply_async(('https://probe.fbrq.cloud/v1/send/', request.data), countdown=countdown, expires=expires)

        task_2 = update_customer_send_task
        task_2.apply_async((request.data,), countdown=expires)

        # for key in redis_instance.keys(request.data[ 'newsletter' ]):
        #     print(redis_instance.get(key))
        return Response(serializer.data)
