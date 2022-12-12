from django.contrib import admin
from .models import Cart, DeliveryCost

#админка корзины и доставки(стоимости доставки)
admin.site.register(Cart)
admin.site.register(DeliveryCost)
