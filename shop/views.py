import paytmchecksum
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Orders, OrderUpdate
import math
import json
from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY = 'Sn7OHM7FOki7r6Pf'


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


# ids = 0


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJSON', '')
        custname = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        custemail = request.POST.get('email', '')
        phoneno = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        order = Orders(items_json=items_json, name=custname, email=custemail, phone=phoneno, address=address, city=city,
                       state=state, zip_code=zip_code, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc='the order has been placed')
        update.save()
        # global ids
        # ids = order.order_id
        # thank = True
        # return render(request, 'shop/checkout.html', {'thank': thank, 'id': order.order_id})
        # Request Paytm to transfer the amount to your Merchant account after user has made the payment
        param_dict = {
            'MID': 'NChOww45804213598876',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': custemail,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = paytmchecksum.generateSignature(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {"param_dict": param_dict})
    return render(request, 'shop/checkout.html', {'states': (
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
        'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
        'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
        'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
        'Vermont',
        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')})


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


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = paytmchecksum.verifySignature(response_dict, MERCHANT_KEY, checksum)
    thank = ''
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            thank = True
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            Orders.objects.get(order_id=response_dict['ORDERID']).delete()
    return render(request, 'shop/handlerequest.html', {'response': response_dict, 'thank': thank})
