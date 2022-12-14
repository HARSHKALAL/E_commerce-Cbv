from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

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

class Carousel(models.Model):
    image=models.ImageField(upload_to="carousel/",blank=True,null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)

    def __str__(self):
         return self.product.name

class Order(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    order_id=models.UUIDField(default = uuid.uuid4,editable=False) 
    total_amount=models.IntegerField()
    order_details =  models.JSONField(default=dict)

