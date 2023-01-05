from rest_framework import serializers

from ..models import Newsletter, Customer, NewsletterStatistic


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = (
            'id',
            'start_launch_date',
            'end_launch_date',
            'customer_filter',
            'message',
            'is_valid',
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class NewsletterStatisticListSerializer(serializers.ModelSerializer):
    newsletter = NewsletterSerializer(read_only=True)
    customer_to_send = CustomerSerializer(many=True, read_only=True)
    customer_send = CustomerSerializer(many=True, read_only=True)

    class Meta:
        model = NewsletterStatistic
        fields = '__all__'


class NewsletterStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsletterStatistic
        fields = '__all__'
