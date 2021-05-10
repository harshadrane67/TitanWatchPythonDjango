from django.urls import path
from .views import ProductListView, ProductDetailView, ProductShopView

urlpatterns = [
    path('', ProductListView.as_view(),name='home'),
    path('shop/',ProductShopView.as_view(),name="shop"),
    path('product/<int:pk>',ProductDetailView.as_view(),name='product-detail')
]
