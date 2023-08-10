from django.contrib import admin
from . models import  Todolist,ListItems

# Register your models here.
admin.site.register(Todolist)
admin.site.register(ListItems)