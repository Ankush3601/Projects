from django.shortcuts import render,redirect,reverse
from.models import Product,Order,OrderItem,ShippingAddress
import datetime



# Create your views here.
def store(request):
    prds=Product.objects.all()
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        itemcount=order.get_cart_count
    else:
        itemcount=0
    dict={"prds":prds,"itemcount":itemcount}
    return render(request,"store/store.html",dict)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.ger_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        itemcount=order.get_cart_count
    else:
        order={'get_cart_count':0,'get_cart_total':0,'shipping':False}
        itemcount=order['get_cart_count']
        items=[]
    dict={"order":order,"items":item,"itemcount":itemcount}
    return render(request,"store/cart.html",dict)
def checkout(request):
    dict={}
    return render(request,"store/checkout.html",dict)

def updateitem(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            if request.POST.get('btnupd'):
                lst = [k for k in request.POST if 'txtqty' in k]
                productId = int(lst[0][6:])
                customer = request.user.customer
                product = Product.objects.get(id=productId)
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
                orderitem.quantity=int(request.POST.get("txtqty"+str(productId)))
                orderitem.save()
                if orderitem.quantity<=0:
                    orderitem.delete()
            elif request.POST.get("btndel"):
                lst=[k for k in request.POST if 'txtqty' in k]
                productId=int(lst[0][6:])
                customer = request.user.customer
                product = Product.objects.get(id=productId)
                order, created = Order.objects.get_or_create(customer=customer, complete=False)
                orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
                orderitem.delete()
            else:
                lst=[k for k in request.POST if 'btn' in k]
                productId=int(lst[0][3:])
                customer=request.user.customer
                product=Product.objects.get(id=productId)
                order,created=Order.objects.get_or_create(customer=customer,complete=False)
                orderitem,created=OrderItem.objects.get_or_create(order=order,product=product)
                orderitem.quantity=orderitem.quantity +1
                orderitem.save()
        else:
            cart=getCookie(request)
            if request.POST.get("btnupd"):
                lst=[k for k in request.POST if 'txtqty' in k]
                productId=int(lst[0][6:])
                cart[productId]=int(request.POST.get("txtqty"+str(productId)))
            elif request.POST.get("btndel"):
                lst = [k for k in request.POST if 'txtqty' in k]
                productId = int(lst[0][6:])
                cart[productId] = 0
            else:
                lst = [k for k in request.POST if 'btn' in k]
                productId = int(lst[0][3:])
                cart[productId]=cart.get(productId,0)+1
            max_age = 365 * 24 * 60 * 60
            expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                                 "%a,%d-%b-%Y %H:%M:%S GMT")
            response = redirect(reverse("cart"))
            response.set_cookie('cart', json.dumps(cart), max_age, expires, path="/")
            return response
    return redirect(reverse("cart"))
def processorder(request):
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        order.transaction_id=datetime.datetime.now().timestamp()
        order.complete=True
        order.save()
        if order.shipping==True:
            ShippingAddress.objects.create(customer=customer,order=order,
                                           address=data['shippinginfo']['address'],
                                           city=data['shippinginfo']['city'],
                                           state=data['shippinginfo']['state'],
                                           zipcode=data['shippinginfo']['zipcode']
                                           )
    else:
        name=data['userinfo']['name']
        email=data['userinfo']['email']
        customer,created=Customer.objects.get_or_create(email=email)
        customer.name=name
        customer.save()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = datetime.datetime.now().timestamp()
        order.complete = True
        order.save()
        dict=cookieCart(request)
        for item in dict['items']:
            product=Product.objects.get(id=item['product']['id'])
            orderitem,created=OrderItem.objects.get_or_create(order=order,product=product)
            orderitem.quantity=item['quantity']
            orderitem.save()
        if order.shipping==True:
            ShippingAddress.objects.create(customer=customer,order=order,
                                           address=data['shippinginfo']['address'],
                                           city=data['shippinginfo']['city'],
                                           state=data['shippinginfo']['state'],
                                           zipcode=data['shippinginfo']['zipcode']
                                           )

    return JsonResponse("order done",safe=False)
