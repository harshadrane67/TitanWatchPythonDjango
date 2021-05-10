from django.contrib import admin
from .models import Order, OrderItem

cart_models = [OrderItem, Order]
admin.site.register(cart_models)
