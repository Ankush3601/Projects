from django.db import models

# Create your models here.
class Welcome(models.Model):
    name = models.CharField(max_length=250)