from django.db import models
from custom_caps.models import Caps, Category


class MagazineDiscount(models.Model):
    DISCOUNT_CHOICES = (
        ('Amount', 'amount'),
        ('Rate', 'rate')
    )
    discount_type = models.CharField(max_length=6,
                                     choices=DISCOUNT_CHOICES,
                                     default="rate",
                                     null=False)
    discount_rate = models.IntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    minimum_purchased_items = models.IntegerField(null=False)
    CHOICE_TO_APPLY = (
        ('Caps', 'caps'),
        ('Category', 'category')
    )
    apply_to = models.CharField(max_length=8,
                                choices=CHOICE_TO_APPLY,
                                default="caps",
                                null=False)
    target_caps = models.ForeignKey(Caps, on_delete=models.SET_NULL, null=True, blank=True)
    target_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID {self.id}: {self.discount_type}({self.discount_amount})'


class MagazineCoupon(models.Model):
    minimum_cart_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_rate_caps = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID {self.id}: {self.minimum_cart_amount}({self.discount_rate_caps})'

