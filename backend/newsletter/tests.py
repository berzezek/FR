from django.test import TestCase
from .models import Newsletter, Customer, NewsletterStatistic
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

logger.info('Test started')


class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(phone_number='1234567890', phone_prefix='+7', tag='test',
                                customer_time_zone='Europe/Moscow')

    def test_customer_creation(self):
        customer = Customer.objects.get(phone_number='1234567890')
        self.assertTrue(isinstance(customer, Customer))
        self.assertEqual(customer.__str__(), customer.phone_number)
        self.assertEqual(customer.get_phone_number(), '71234567890')
        self.assertEqual(customer.get_full_phone_number(), '+771234567890')


class NewsletterModelTests(TestCase):
    time_now = timezone.now()

    def setUp(self):
        Newsletter.objects.create(
            start_launch_date=self.time_now - timezone.timedelta(days=1),
            end_launch_date=self.time_now + timezone.timedelta(days=1),
            customer_filter='test',
            message='test_is_valid',
        )
        Newsletter.objects.create(
            start_launch_date=self.time_now + timezone.timedelta(days=1),
            end_launch_date=self.time_now,
            customer_filter='test',
            message='test_is_not_valid',
        )

    def test_newsletter_creation(self):
        ns_1 = Newsletter.objects.get(message='test_is_valid')
        ns_2 = Newsletter.objects.get(message='test_is_not_valid')
        self.assertEqual(ns_1.start_launch_date, self.time_now - timezone.timedelta(days=1))
        self.assertEqual(ns_1.end_launch_date, self.time_now + timezone.timedelta(days=1))
        self.assertEqual(ns_1.customer_filter, 'test')
        self.assertEqual(ns_1.message, 'test_is_valid')
        self.assertEqual(ns_1.is_valid(), True)
        self.assertEqual(ns_2.is_valid(), False)


class NewsletterStatisticModelTests(TestCase):
    def setUp(self):
        customer = Customer.objects.create(phone_number='1234567890', phone_prefix='+7', tag='test',
                                           customer_time_zone='Europe/Moscow')
        newsletter = Newsletter.objects.create(start_launch_date=timezone.now() - timezone.timedelta(days=1),
                                               end_launch_date=timezone.now() + timezone.timedelta(days=1),
                                               customer_filter='test', message='test')

        ns = NewsletterStatistic.objects.create(newsletter=newsletter)
        ns.customer.add(customer)

    def test_newsletter_statistic_creation(self):
        ns = NewsletterStatistic.objects.get(id=1)
        self.assertEqual(ns.customer.count(), 1)
        self.assertEqual(ns.newsletter.message, 'test')

