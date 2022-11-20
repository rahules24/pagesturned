from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Orders, OrderUpdate
import math
import json


def index(request):
    allprods = []
    catprods = Product.objects.values('category')
    price = Product.objects.values('price')
    print(price)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        print(prod)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        # nn = -1
        # li = []
        # for i in range(1, len(prod)):
            # nn = nn + 4
            # if nn <= len(prod):
            #     i += 1
            #     li.append(nn)
        allprods.append([price, prod, range(1, nSlides), nSlides])
    # products = Product.objects.all()
    # print(products)
    # print(li)
    # params = {'no_of_slides': nslides, 'ranges': range(1, nslides), 'product': products, 'counts': li}
    # allprods = [[products, range(1, nslides), li], [products, range(1, nslides), li]]
    params = {'allprod': allprods}
    return render(request, "shop/index.html", params)


def prodview(request, myid):
    # Fetching product details using its id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html', {'viewprod': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJSON', '')
        custname = request.POST.get('name', '')
        custemail = request.POST.get('email', '')
        phoneno = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        order = Orders(items_json=items_json, name=custname, email=custemail, phone=phoneno, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc='the order has been placed')
        update.save()
        thank = True
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': order.order_id})
    return render(request, 'shop/checkout.html', {'states': ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')})


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')
