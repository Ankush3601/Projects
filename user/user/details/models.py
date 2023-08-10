from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    password = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.first_name
