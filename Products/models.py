from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return  f'{self.gender} {self.name} Categories'


class Brand(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(unique=True,blank=True)

    def __str__(self):
        return f'{self.name}'

class Collection(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    img = models.ImageField(upload_to='product_img')
    name = models.CharField(max_length=120)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True,null=True)
    offer_val = models.IntegerField(blank=True,null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.offer_val = self.cal_offer()
        super(Products, self).save(*args, **kwargs)

    def cal_offer(self):
        if self.offer:
            try:
                offer_val = self.price - ((self.discount*self.price)/100)
                return offer_val
            except KeyError:
                print("Error in Product model cal_offer method")
                return 0
        else:
            return 0

class ProductDetails(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL,null=True)
    product = models.OneToOneField(Products,on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    warranty = models.TextField()
    function = models.CharField(max_length=100)
    dial_color = models.CharField(max_length=10)
    case_shape = models.CharField(max_length=10)
    case_material = models.CharField(max_length=50)
    case_thickness = models.FloatField()
    case_length = models.FloatField()
    case_width = models.FloatField()

    def __str__(self):
        return f'{self.product.name}'




