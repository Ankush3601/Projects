from.views import courses,course_detail,endpoints,Coursedetail
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns=[
    path("",endpoints),
    path("courses/",courses),
    path("courses/<str:cname>/",course_detail),
    path("courses/<str:cname>/",Coursedetail.as_view()),
    path("categories/",categories),
    path("token/",TokenObtainPairView.as_view())
]