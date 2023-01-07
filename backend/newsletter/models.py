import time

from django.db import models


class Newsletter(models.Model):
    start_launch_date = models.DateTimeField()
    end_launch_date = models.DateTimeField()
    customer_filter = models.CharField(max_length=128)
    message = models.TextField()

    def is_valid(self):
        return time.mktime(self.start_launch_date.timetuple()) < time.mktime(self.end_launch_date.timetuple()) and \
               time.time() < int(time.mktime(self.end_launch_date.timetuple()))

    def __str__(self):
        return f'Start date: {self.start_launch_date}, Message: {self.message}'


class Customer(models.Model):
    phone_number = models.CharField(max_length=32, unique=True)
    phone_prefix = models.CharField(max_length=32)
    tag = models.CharField(max_length=128)
    customer_time_zone = models.CharField(max_length=128)

    def get_phone_number(self):
        return f'7{self.phone_number}'

    def get_full_phone_number(self):
        return f'{self.phone_prefix}{self.get_phone_number()}'

    def __str__(self):
        return self.phone_number


class NewsletterStatistic(models.Model):
    customer = models.ManyToManyField(Customer, blank=True, related_name='customers')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)

