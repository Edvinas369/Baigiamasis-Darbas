from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import User
# Create your views here.

def index(request):
    return HttpResponse('User App')

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        error = False
        if not password or password != password2:
            messages.error(request, _('Slaptažodis netinkamas arba neįvestas'))
            error = True
        if not username or User.objects.filter(username=username).exsisting():
            messages.error(request, _('Klientas su tokiu prisijungimo {} varduo jau egzistuoja').format(username))
            error = True            
        if not email or User.objects.filter(email=email).exists():
            messages.error(request, _('Klientas su tokiu el.paštu {}  jau egzistuoja').format(email))
            error=True
        if error:
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, _('Klientas {} buvo sėkmingai priregistruotas').format(email))
            return redirect('index')
    return render(request, 'register.html')