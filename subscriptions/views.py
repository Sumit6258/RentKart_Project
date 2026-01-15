from rest_framework.viewsets import ModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer
from .permissions import IsAdminOnly
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

class SubscriptionAdminViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAdminOnly]

    @action(detail=True, methods=['post'])
    def mark_paid(self, request, pk=None):
        subscription = self.get_object()
        subscription.payment_status = 'paid'
        subscription.save()
        return Response({"message": "Payment marked as PAID"})


class SubscriptionCustomerViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        if phone:
            return Subscription.objects.filter(customer__phone=phone)
        return Subscription.objects.none()
