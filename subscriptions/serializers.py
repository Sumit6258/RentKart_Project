from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.name')
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Subscription
        fields = '__all__'
