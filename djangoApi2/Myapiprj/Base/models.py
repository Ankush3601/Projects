from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name


class Courses(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=500,null=True,blank=True)
    cost=models.IntegerField(default=0)
    isonline=models.BooleanField(default=False)
    def __str__(self):
      return self.name
