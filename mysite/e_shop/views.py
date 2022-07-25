from django.http import HttpResponse
from django.shortcuts import render
from e_shop.models import Setting
from e_shop.models import Setting
from product.models import Category, Product
from django.utils.translation import gettext as _
from django.db.models import Q
from product.models import Product


def index(request):
    setting = Setting.objects.get(pk=1)
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


def category_products(request,id,slug):
    products = Product.objects.filter (category_id=id)
    return HttpResponse(products)


from django.db.models import Q

def search(request):

    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'search_results': search_results, 'query': query})