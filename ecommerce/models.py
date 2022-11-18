from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE = (
    ('merchant', 'MERCHANT'),
    ('consumer', 'CONSUMER'),
)
    role = models.CharField(max_length=50, choices=ROLE,null=True)

class Comapny(models.Model):
    name=models.CharField(max_length=100)
    Address=models.CharField(max_length=255)
    gst_no=models.CharField(max_length=15)

    def __str__(self):
         return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)    

    def __str__(self):
         return self.name

class MerchantFirm(models.Model):
    firm_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
         return self.firm_name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    text=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="products/",blank=True,null=True)
    sold_by=models.ManyToManyField(MerchantFirm)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    category = models.ManyToManyField(Category,related_name='products')
    stock_quantity = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name

    





