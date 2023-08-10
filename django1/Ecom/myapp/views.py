from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    dict={"Name":"Ankush","Married":True ,"Qual" :["BCA", "MCA"]}

    return render(request,"hello.html",dict)
def products(request):
    return HttpResponse("This is my product list")