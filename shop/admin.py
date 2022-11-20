from django.contrib import admin
from .models import Product, Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
