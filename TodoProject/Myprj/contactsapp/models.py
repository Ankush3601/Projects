from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    income = models.DecimalField(max_digits=6,decimal_places=2)
    dateofbirth = models.DateField(null=True)
    photo = models.CharField(max_length=250000,null=True)
    is_married = models.BooleanField()
    membershipchoice= [('G',"Gold"),('S',"Silver"),('P',"Platinum")]
    memberships = models.CharField(max_length=1,choices=membershipchoice,default='G')
