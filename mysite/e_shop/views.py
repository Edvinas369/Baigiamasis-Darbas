from django.shortcuts import render
from e_shop.models import Setting

# Create your views here.


def index(request):
    return render(request, 'index.html')


def checkout(request):
    return render(request, 'checkout.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'contactus.html', context)


def cart(request):
    return render(request, 'cart.html')


def refund(request):
    return render(request, 'refund.html')


def product_details(request):
    return render(request, 'product_details.html')
