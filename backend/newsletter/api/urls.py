from .views import NewsletterViewSet, CustomerViewSet, NewsletterStatisticViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('newsletter', NewsletterViewSet, basename='newsletter')
router.register('customer', CustomerViewSet, basename='customer')
router.register('newsletter-statistic', NewsletterStatisticViewSet, basename='newsletterStatistic')

urlpatterns = router.urls
