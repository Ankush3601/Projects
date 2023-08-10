from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data=["courses/","courses/:cname"]
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def courses(request):
    qry=request.GET.get('srcstr')
    if qry==None:
        qry=''
    data=Courses.objects.filter(name__icontains=qry)
    serializer=CourseSerializer(data,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def categories(request):
    data = Category.objects.all()
    serializer=CategorySerializer(data,many=True)
    return Response(serializer.data)
@api_view(['GET','PUT','DELETE'])
def course_detail(request,cname):
    data = Courses.objects.get(name=cname)
    if request.method=='GET':
        serializer = CourseSerializer(data, many=False)
    return Response(serializer.data)
    if request.method=='PUT':
        data.name=request.data['name']
        data.description=request.data['description']
        data.cost=request.data['cost']
        data.isonline=request.data['isonline']
        data.save
        serializer = CourseSerializer(data, many=False)
    return Response(serializer.data)
    if request.method=='DELETE':
        data.data()
    return Response("Course has been deleted")
class Coursedetail(APIView):
    def get(self,request,cname):
        crs = self.get.object(cname)
        serializer=CourseSerializer(crs,many=False)
        return Response(serializer.data)
    def put(self,request,cname):
        crs = self.get.object(cname)
        crs.name =request.data.get('name')
        crs.description = request.data.get('description')
        crs.cost = request.data.get('cost')
        crs.isonline = request.data.get('isonline')
        crs.save()
        serializer = CourseSerializer(crs, many=False)
        return Response(serializer.data)
    def delete(self, request,cname):
        crs = self.get.object(cname)
        crs.delete()
        return Response("Course has been deleted")
    def get_object(self,cname):
        try:
            crs=courses.objects.get(name=cname)
            return crs
        except:
            return JsonResponse("Course not found")