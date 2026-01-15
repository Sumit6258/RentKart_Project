from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionAdminViewSet, SubscriptionCustomerViewSet

router = DefaultRouter()

router.register(
    'admin/subscriptions',
    SubscriptionAdminViewSet,
    basename='admin-subscriptions'
)
router.register(
    'subscriptions',
    SubscriptionCustomerViewSet,
    basename='customer-subscriptions'
)

urlpatterns = [
    path('', include(router.urls)),
]
