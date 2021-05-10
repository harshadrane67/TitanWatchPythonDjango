from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order, Shipping_client
from Products.models import ProductDetails
from Accounts.models import Profile, Address
from django.contrib import messages
from django.views.generic import ListView
from Accounts.forms import Shiping_cust_form, AddressForm
from datetime import datetime

@login_required
def display_cart(request):
    profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(profile=profile,is_ordered=False).first()
    if order == None:
        empty = True
    else:
        empty = not order.get_all_items().exists()
    return render(request,'Cart/cart.html',{'order':order, 'empty':empty })


@login_required
def add_to_cart(request, pro_id):
    product = get_object_or_404(ProductDetails, id=pro_id)
    profile = get_object_or_404(Profile, user=request.user)
    order_item, created = OrderItem.objects.get_or_create(product=product,profile=profile,is_ordered=False)
    order, created = Order.objects.get_or_create(profile=profile,is_ordered=False)
    if order_item in order.get_all_items():
        messages.error(request,'Item already present in cart')
        return redirect('home')
    else:
        order.items.add(order_item)
        messages.success(request,'Item Successfuly added to cart')
        
    return redirect('display-cart')


@login_required
def delete_from_cart(request, order_item_id):
    profile = get_object_or_404(Profile, user=request.user)
    try:
        order_item = OrderItem.objects.get(id=order_item_id,profile=profile,is_ordered=False)
        order_item.delete()
        messages.success(request,'Item Successfuly deleted from cart')
        return redirect('display-cart')
    except OrderItem.DoesNotExist:
        messages.error(request,'Item is not present in cart')
        return redirect('display-cart')

@login_required
def select_address(request):
    address = Address.objects.filter(user=request.user)
    return render(request, 'Cart/select_address.html',{'address':address})

@login_required
def checkout(request, add_id):
    profile = get_object_or_404(Profile, user=request.user)
    address = request.user.address_set.filter(id=add_id).first()
    order, created = Order.objects.get_or_create(profile=profile,is_ordered=False)
    if address != None:
        if request.method == 'POST':
            ship_c_form = Shiping_cust_form(request.POST)
            a_form = AddressForm(request.POST, instance=address)
            if ship_c_form.is_valid() and a_form.is_valid():
                sc_form = ship_c_form.save(commit=False)
                sc_form.address = address
                sc_form.placed = True
                sc_form.profile = profile
                sc_form.shipping_status = 'Order_placed'
                for item in order.get_all_items():
                    item.is_ordered = True
                    item.date_ordered = datetime.now()
                    item.save()
                order.is_ordered = True
                order.date_ordered = datetime.now()
                order.save()
                sc_form.order = order
                sc_form.save()
                a_form.save()
                messages.success(request,'Order placed successfuly ')
                return redirect('order-detail', order_id=order.id)
        else:
            ship_c_form = Shiping_cust_form()
            a_form = AddressForm(instance=address)
    else:
        messages.error(request,'Address not found')
        return redirect('profile-address')
    
    contex = {
        'sc_form':ship_c_form,
        'a_form':a_form,
        'order': order
        }
    return render(request, 'Cart/checkout.html',contex)

def orders(request):
    profile = get_object_or_404(Profile, user=request.user)
    orders = Order.objects.filter(profile=profile,is_ordered=True)
    return render(request,'Cart/orders.html',{'orders':orders, 'empty': not orders.exists()})


@login_required
def order_details(request, order_id):
    profile = get_object_or_404(Profile, user=request.user)
    try:  
        order = Order.objects.filter(id=order_id).first()
    except Order.DoesNotExist:
        messages.error(request, "There is no order placed")
        redirect('home')
    shipping_client_info = Shipping_client.objects.filter(profile=profile,order=order,placed=True).first()
    contex = {
        'shipping_client': shipping_client_info,
        'order': order
    }
    return render(request, 'Cart/confirmation.html',contex)
    
    


