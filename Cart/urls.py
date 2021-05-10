from django.urls import path
from .views import add_to_cart, delete_from_cart, display_cart, select_address, checkout, orders, order_details

urlpatterns = [
    path('',display_cart,name='display-cart'),
    path('add-to-cart/<int:pro_id>/',add_to_cart,name='add-to-cart'),
    path('delete-from-cart/<int:order_item_id>/',delete_from_cart,name='delete-from-cart'),
    path('select-shipping-address/',select_address,name='select-address'),
    path('checkout/<int:add_id>/',checkout,name='checkout'),
    path('profile/orders',orders,name='profile-orders'),
    path('order-detail/<int:order_id>/',order_details,name='order-detail')
]