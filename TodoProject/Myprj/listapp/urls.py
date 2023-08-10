from django.urls import path
from . views import render

from.views import alllists, detail
from.models import Todolist
urlpatterns=[
    path("", alllists),
    path("<int:id>", detail)
]
