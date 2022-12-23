from datetime import datetime

from django.db import models


class Newsletter(models.Model):
    start_launch_date = models.DateTimeField()
    end_launch_date = models.DateTimeField()
    customer_filter = models.CharField(max_length=100)
    message = models.TextField()
    #
    # def expired_mailing(self):
    #     return self.end_launch_date < datetime.now()

    def __str__(self):
        return f'{self.start_launch_date} - {self.end_launch_date}'


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
