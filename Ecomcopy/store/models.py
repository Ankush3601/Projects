from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    digital=models.BooleanField(default=False,null=True)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def imageurl(self):
        try:
            url=self.image.url
        except:
            url="/images/placeholder.png"
        return url

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
    @property
    def shipping(self):
        shipping=False
        items=self.orderitem_set.all()
        for item in items:
            if item.product.digital==False:
                shipping=True
        return shipping

    @property
    def get_cart_count(self):
        items=self.orderitem_set.all()
        cnt=sum([item.quantity for item in items])
        return cnt
    @property
    def get_cart_total(self):
        items=self.orderitem_set.all()
        tot=sum([item.get_total for item in items])
        return tot


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        return self.quantity*self.product.price


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address=models.CharField(max_length=500,null=False)
    city = models.CharField(max_length=500, null=False)
    state = models.CharField(max_length=500, null=False)
    zipcode = models.CharField(max_length=500, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address


