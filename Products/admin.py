from django.contrib import admin
from .models import Categories, Brand, Collection, Products, ProductDetails

product_models = [Categories,Brand,Collection,Products,ProductDetails]
admin.site.register(product_models)
