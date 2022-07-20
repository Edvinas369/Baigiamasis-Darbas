from django.http import HttpResponse
from django.shortcuts import render
from e_shop.models import Setting

# Create your views here.
from e_shop.models import Setting
from product.models import Category, Product


def index(request):
    setting = Setting.objects.filter(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4] # Pirmi keturi produktai 
    products_latest = Product.objects.all().order_by('-id')[:4] # Paskutiniai 4 produktai 
    products_picked = Product.objects.all().order_by('?')[:4] # random 
    page ="index"
    context={'setting': setting,
            'category': category,
            'page': page,
            'products_slider' : products_slider,
            'products_latest' : products_latest,
            'products_picked' : products_picked,
                 }
    return render(request,'index.html', context)


def checkout(request):
    return render(request, 'checkout.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    setting = Setting.objects.filter(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    setting = Setting.objects.filter(pk=1)
    context = {'setting': setting}
    return render(request, 'contactus.html', context)


def cart(request):
    return render(request, 'cart.html')


def refund(request):
    return render(request, 'refund.html')


def product_details(request):
    return render(request, 'product_details.html')


def category_products(request,id,slug):
    products = Product.objects.filter (category_id=id)
    return HttpResponse(products)