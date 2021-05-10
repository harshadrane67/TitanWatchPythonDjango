from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Address
from Cart.models import Shipping_client


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email']


class ProfileUpdateForm(forms.ModelForm):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages = { 'required':"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other')
    )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta():
        model = Profile
        fields = ['gender','phone_number','img'] 


class AddressForm(forms.ModelForm):
    ADD_TYPE_CHOISES = (
        ('Home','Home'),
        ('Office','Office')
    )
    address = forms.Textarea()
    town = forms.CharField(max_length=120)
    city = forms.CharField(max_length=120)
    pin = forms.IntegerField()
    state = forms.CharField(max_length=120)
    default = forms.BooleanField(required=False)
    type_add = forms.ChoiceField(widget=forms.RadioSelect, choices=ADD_TYPE_CHOISES,required=False)

    class Meta():
        model = Address
        fields = ['address','town','city','pin','state','default','type_add']


class Shiping_cust_form(forms.ModelForm):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages = { 'required':"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})

    class Meta():
        model = Shipping_client
        fields = ['first_name', 'last_name','email','phone_number']