from django.db import models
from accounts.models import Customer
from catalog.models import Product
from datetime import timedelta

class Subscription(models.Model):

    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            if self.product.subscription_type == 'weekly':
                self.end_date = self.start_date + timedelta(days=7)
                self.total_cost = self.product.price
            elif self.product.subscription_type == 'monthly':
                self.end_date = self.start_date + timedelta(days=30)
                self.total_cost = self.product.price
            elif self.product.subscription_type == 'quarterly':
                self.end_date = self.start_date + timedelta(days=90)
                self.total_cost = self.product.price * 3
            elif self.product.subscription_type == 'yearly':
                self.end_date = self.start_date + timedelta(days=365)
                self.total_cost = self.product.price * 12

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"
