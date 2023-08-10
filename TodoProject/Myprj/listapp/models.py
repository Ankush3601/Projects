from django.db import models

# Create your models here.
class Todolist(models.Model):
    name=models.CharField(max_length=250)
    def __str__ (self):
        return self.name

class ListItems(models.Model):
    text=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    todolist=models.ForeignKey(Todolist,on_delete=models.CASCADE)
    def __str__ (self):
        return self.text