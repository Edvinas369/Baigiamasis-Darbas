from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from . forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profiles/profile.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        error = False
        if not password or password != password2:
            messages.error(request, 'The password is invalid or not entered')
            error = True
        if not username or User.objects.filter(username=username).exists():
            messages.error(request, 'A client with this login name {} already exists'.format(username))
            error = True
        if not email or User.objects.filter(email=email).exists():
            messages.error(request, 'A customer with this email {} already exists'.format(email))
            error = True
        if error:
            return redirect('register')
        else:
            User.objects.create_user(
                username=username, email=email, password=password)
            messages.success(request, 'Customer {} was successfully registered'.format(email))
            return redirect('/')
    return render(request, 'register.html')


@login_required
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'user profile was updated successfully')
            return redirect(reverse_lazy('profile'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profiles/profile_update.html', {'u_form': u_form, 'p_form': p_form})
