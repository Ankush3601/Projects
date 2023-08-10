from django.shortcuts import render
from django.http import HttpResponse
from.models import Todolist
from.models import ListItems


# Create your views here.
def alllists(request):
    ls= Todolist.objects.all()
    return render (request,"home.html",{"data":ls})

def detail(request,id):
    l= Todolist.objects.get(id=id)
    item=l.ListItems_set.all()
    return HttpResponse(item)