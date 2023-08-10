from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def endpoints(request):
    data=["courses/","courses/:cname"]
    return JsonResponse(data,safe=False)
def courses(request):
    data=["python","PHP","Full Stack"]
    return JsonResponse(data, safe=False)
def course_detail(request,cname):
    data="Details for course"+cname
    return JsonResponse(data, safe=False)