from .views import endpoints,courses,course_detail
from django.urls import path
urlpatterns=[
   path("",endpoints),
   path("courses/",courses),
   path("courses/<str:cname>/",course_detail)
]