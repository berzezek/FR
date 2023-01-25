from .models import NewsletterStatistic


def update_customer_list(customer_received_list, newsletter_statistic_id):
    ns = NewsletterStatistic.objects.get(id=newsletter_statistic_id)
    for customer in customer_received_list:
        ns.customer.add(customer[ 'id' ])
    ns.save()