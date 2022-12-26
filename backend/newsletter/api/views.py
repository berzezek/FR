from .serializers import NewsletterSerializer, CustomerSerializer, NewsletterStatisticSerializer
from ..models import Newsletter, Customer, NewsletterStatistic
from rest_framework import viewsets


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class NewsletterStatisticViewSet(viewsets.ModelViewSet):
    queryset = NewsletterStatistic.objects.all()
    serializer_class = NewsletterStatisticSerializer
