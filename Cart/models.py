from django.db import models
from django.contrib.auth.models import User
from Accounts.models import Profile, Address
from django.core.validators import RegexValidator
from Products.models import ProductDetails



class OrderItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=None,null=True)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True,blank=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.product.name}'

    def save(self, *args, **kwargs):
        if self.product.product.offer:
            self.price = self.quantity * self.product.product.offer_val
        else:
            self.price = self.quantity * self.product.product.price
        
        super(OrderItem, self).save(*args, **kwargs)


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.profile} Order({self.pk})'

    def get_all_items(self):
        return self.items.all()

    def get_total_price(self):
        return sum(item.price for item in self.items.all())


class Shipping_client(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default=None,null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.OneToOneField(Order,on_delete=models.SET_NULL,null=True)
    placed = models.BooleanField(default=False)
    shipping_status = models.CharField(max_length=50,default='None',null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} Customer'