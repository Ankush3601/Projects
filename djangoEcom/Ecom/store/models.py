from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    digital=models.BooleanField(default=False,null=True)
    image=models.ImageField(null=True,blank=True)
def __str__ (self):
    return self.name
    @property
    def imageurl(self):
        try:
            url=self.image.url
        except:
            url="/images/cart 0.png"
            return url
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
def __str__(self):
        return self.name
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=250)
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date_added=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.address
class ShippingAddress(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    custom=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address=models.CharField(max_length=500,null=False)
    city=models.CharField(max_length=500,null=False)
    state=models.CharField(max_length=200,null=False)
    zipcode=models.CharField(max_length=200,null=False)
    date_added=models.DateField(auto_now_add=True)
def __str__(self):
    return self.address