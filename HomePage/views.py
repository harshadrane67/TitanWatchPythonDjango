from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Products.models import Products, ProductDetails

class ProductListView(ListView):
    model = Products
    template_name = 'HomePage/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = ProductDetails
    template_name = 'HomePage/product_details.html'
    context_object_name = 'products_detail'

class ProductShopView(ListView):
    model = Products
    template_name = 'HomePage/shop.html'
    context_object_name = 'products'


