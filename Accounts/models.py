from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
#from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,null=True,default='None')
    img = models.ImageField(default='default.jpg', upload_to='profile_imgs')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        p_img = Image.open(self.img.path)

        if p_img.width > 200 or p_img.height > 200:
            output_size = (200,200)
            p_img.thumbnail(output_size)
            p_img.save(self.img.path)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    town = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    pin = models.IntegerField()
    state = models.CharField(max_length=120)
    default = models.BooleanField(default=False,blank=True)
    type_add = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f'{self.user.username} Address '



