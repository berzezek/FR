from rest_framework import serializers
from ..models import Newsletter, Customer


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        # fields = ('id', 'start_launch_date', 'end_launch_date', 'customer_filter', 'message', 'expired_mailing')
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
