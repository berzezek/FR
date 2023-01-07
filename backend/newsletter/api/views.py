from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from ..tasks import send_newsletter_task

from .serializers import NewsletterSerializer, CustomerSerializer, NewsletterStatisticSerializer, \
    NewsletterStatisticListSerializer
from ..models import Newsletter, Customer, NewsletterStatistic


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class NewsletterStatisticViewSet(viewsets.ModelViewSet):
    queryset = NewsletterStatistic.objects.all()
    serializer_class = NewsletterStatisticSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = NewsletterStatisticListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # send_newsletter
        newsletter_statistic_id = serializer.instance.id
        newsletter = Newsletter.objects.get(id=request.data[ 'newsletter' ])
        start_launch_date = newsletter.start_launch_date
        end_launch_date = newsletter.end_launch_date
        countdown = (start_launch_date - timezone.now()).total_seconds()
        expires = (end_launch_date - timezone.now()).total_seconds()
        if countdown < 0:
            countdown = 0
        if expires < 0:
            return Response({'error': 'End launch date is in the past'})

        send_newsletter_task.apply_async(
            ('https://probe.fbrq.cloud/v1/send/', request.data, newsletter_statistic_id), countdown=countdown,
                                         expires=expires)
        return Response(serializer.data, status=201)
