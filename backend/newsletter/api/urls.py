from .views import NewsletterViewSet, CustomerViewSet, NewsletterStatisticViewSet, CustomerStatisticViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('newsletter', NewsletterViewSet, basename='newsletter')
router.register('customer', CustomerViewSet, basename='customer')
router.register('newsletter-statistic', NewsletterStatisticViewSet, basename='newsletterStatistic')
router.register('customer-statistic', CustomerStatisticViewSet, basename='customerStatistic')

urlpatterns = router.urls
