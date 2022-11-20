from django.shortcuts import render
from .models import Contact


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        custname = request.POST.get('name', '')
        custemail = request.POST.get('email', '')
        phoneno = request.POST.get('phone', '')
        qdesc = request.POST.get('desc', '')
        contactdet = Contact(name=custname, email=custemail, phone=phoneno, desc=qdesc)
        contactdet.save()
        return render(request, 'contact.html', {'query': True})
    return render(request, 'contact.html')


def search(request):
    return render(request, 'search.html')