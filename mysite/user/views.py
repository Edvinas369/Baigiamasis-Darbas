from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.


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
            messages.error(request, ('The password is invalid or not entered'))
            error = True
        if not username or User.objects.filter(username=username).exists():
            messages.error(request, ('A client with this login name {} already exists').format(username))
            error = True            
        if not email or User.objects.filter(email=email).exists():
            messages.error(request, ('A customer with this email {} already exists').format(email))
            error=True
        if error:
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, ('Customer {} was successfully registered').format(email))
            return redirect('e_shop')
    return render(request, 'register.html')



@login_required
def profile(request):
    return render(request, 'profile.html')

