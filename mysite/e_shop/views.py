from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
 
def checkout(request):
<<<<<<< HEAD
    return render(request, 'checkout.html')
=======
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')
>>>>>>> b4afd4b4b704e09f571a00eada66fb1cba28c5d0
