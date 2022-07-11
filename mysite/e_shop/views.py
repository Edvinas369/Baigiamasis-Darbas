from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
 
def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def refund(request):
    return render(request, 'refund.html')
