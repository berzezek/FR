from django.contrib import admin
from .models import Newsletter, Customer, NewsletterStatistic, CustomerStatistic

# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Customer)
admin.site.register(NewsletterStatistic)
admin.site.register(CustomerStatistic)