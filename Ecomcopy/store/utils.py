import json
import datetime
from django.http import HttpResponse
from .models import Product
def getCookie(request):
    try:
        cart=json.loads(request.COOKIES['cart'])
    except:
        cart={}
        max_age=365*24*60*60
        expires=datetime.datetime.strftime(datetime.datetime.utcnow()+datetime.timedelta(seconds=max_age),"%a,%d-%b-%Y %H:%M:%S GMT")
        response=HttpResponse("")
        response.set_cookie('cart',json.dumps(cart),max_age,expires,path="/")
        cart = json.loads(request.COOKIES['cart'])
    return cart

def cookieCart(request):
    cart=getCookie(request)
    items=[]
    order = {'get_cart_count': 0, 'get_cart_total': 0, 'shipping': False}
    for t in cart:
        if cart[t]!=0:
            product=Product.objects.get(id=t)
            total=product.price*cart[t]
            item={'product':{'id':product.id,'name':product.name,'price':product.price,'imageurl':product.imageurl},
                  'quantity':cart[t],
                  'get_total':total
                  }
            items.append(item)
            order['get_cart_count']+=cart[t]
            order['get_cart_total']+=total
            if product.digital==False:
                order['shipping']=True
    itemcount=order['get_cart_count']
    return {"order": order, "items": items, "itemcount": itemcount}
