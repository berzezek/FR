import time
from datetime import date

from django.db import models


class Newsletter(models.Model):
    start_launch_date = models.DateTimeField()
    end_launch_date = models.DateTimeField()
    customer_filter = models.CharField(max_length=100)
    message = models.TextField()

    def is_valid(self):
        return int(time.mktime(self.start_launch_date.timetuple())) < time.time() < int(time.mktime(self.end_launch_date.timetuple()))

    def __str__(self):
        return f'Start date: {self.start_launch_date}, Message: {self.message}'


class Customer(models.Model):
    phone_number = models.CharField(max_length=10, unique=True)
    phone_prefix = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    customer_time_zone = models.CharField(max_length=100)

    def get_phone_number(self):
        return f'7{self.phone_number}'

    def get_full_phone_number(self):
        return f'{self.phone_prefix}{self.get_phone_number()}'

    def __str__(self):
        return self.phone_number


class NewsletterStatistic(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    send_date = models.DateTimeField(auto_now_add=True)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.newsletter} - {self.customer}'
