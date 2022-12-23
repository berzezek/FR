from .serializers import NewsletterSerializer, CustomerSerializer
from ..models import Newsletter, Customer
from rest_framework import viewsets


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
