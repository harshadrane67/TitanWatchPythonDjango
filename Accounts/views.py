from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, AddressForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Address, Profile
from Cart.models import Order


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Created new Account for {username} ')
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'Accounts/register.html', {'form': form})


def logout(request):
    messages.success(request, f'{request.user.username} Successfuly Logout !')
    auth.logout(request)
    return redirect('home')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Accounts/profile_update.html', context)

@login_required()
def profile(request):
    address = Address.objects.filter(user=request.user)
    profile = get_object_or_404(Profile, user=request.user)
    orders = Order.objects.filter(profile=profile,is_ordered=True).order_by('-date_ordered')
    return render(request, 'Accounts/profile.html',{'address':address,'orders':orders, 'empty': not orders.exists()})

@login_required
def address(request):
    address = Address.objects.filter(user=request.user)
    return render(request, 'Accounts/address.html',{'address':address})


@login_required()
def address_from(request):
    if request.method == "POST":
        a_form = AddressForm(request.POST)
        if a_form.is_valid():
            adds = a_form.save(commit=False)
            adds.user = request.user
            adds.save()
            messages.success(request, f'Address Saved')
            return redirect('profile')
    else:
        a_form = AddressForm()
    return render(request,'Accounts/address_form.html',{'a_form':a_form})

@login_required()
def address_update(request, add_id):
    address = request.user.address_set.filter(pk=add_id).first()
    if address != None:
        if request.method == "POST":
            a_form = AddressForm(request.POST, instance=address)
            if a_form.is_valid():
                a_form.save()
                messages.success(request, 'Address Updated')
                return redirect('profile-address')
        else:
            a_form = AddressForm(instance=address)
    else:
        messages.error(request,'Address not found')
        return redirect('profile-address')
    
    return render(request,'Accounts/address_form.html',{'a_form':a_form})
            
@login_required()
def address_delete(request, add_id):
    user = request.user
    address = user.address_set.filter(pk=add_id).first()
    if address != None:
        address.delete()
        messages.success(request,'Address Deleted')
    else:
        messages.error(request, 'Address not found')  
    return redirect('profile-address')
