from .views import NewsletterViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('newsletter', NewsletterViewSet, basename='newsletter')
router.register('customer', CustomerViewSet, basename='customer')

urlpatterns = router.urls
