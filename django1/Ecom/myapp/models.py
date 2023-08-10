from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateField(auto_now=True)
    SKU = models.CharField(max_length=250, primary_key=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    dob = models.DateField(null=True)
    membership_choice = [('B', "Bronze"), ('S', "Silver"), ('G', "Gold")]
    membership=models.CharField(max_length=1, choices=membership_choice, default='B')

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now=True)
    payment_choice = [('p', "Pending"), ('C', "Completed"), ('F', "Failed")]
    payment_status = models.CharField(max_length=1,choices=payment_choice, default='P')

class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

Customer = models.OneToOneField(Customer,on_delete= models.CASCADE,primary_key=True)
Customer = models.ForeignKey(Customer,on_delete =models.CASCADE,primary_key=True)



