from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryAdminViewSet,
    CategoryPublicViewSet,
    ProductAdminViewSet,
    ProductPublicViewSet
)

router = DefaultRouter()

# Admin routes
router.register(
    'admin/categories',
    CategoryAdminViewSet,
    basename='admin-categories'
)
router.register(
    'admin/products',
    ProductAdminViewSet,
    basename='admin-products'
)

# Public routes
router.register(
    'categories',
    CategoryPublicViewSet,
    basename='public-categories'
)
router.register(
    'products',
    ProductPublicViewSet,
    basename='public-products'
)

urlpatterns = [
    path('', include(router.urls)),
]
