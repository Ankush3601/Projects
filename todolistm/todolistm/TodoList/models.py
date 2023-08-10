from django.db import models
from django.utils import timezone


# Create your models here.
class TodoCategory(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default = timezone.now)