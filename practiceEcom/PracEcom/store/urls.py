from django.urls import path
from .views import store,cart,checkout,updateitem,processorder

urlpatterns=[
    path("",store,name="store"),
    path("cart/",cart,name="cart"),
    path("checkout/",checkout,name="checkout"),
    path("updateitem/",updateitem,name="updateitem"),
    path("processorder/",processorder,name="processorder")
]