from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Category
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct
from django.contrib import messages
from django.http import HttpResponseRedirect
import string
import random
from user_profile.models import Profile


def order(request):
    return render(request, 'order.html')


@login_required
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Product added to Shopcart')

    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, 'Product added to Shopcart')
        return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for product in shopcart:
        total += product.product.price * product.quantity
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               }
    return render(request, 'cart_products.html', context)


@login_required
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Your item deleted form Shopcart.')
    return redirect('/shopcart')


def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for product in shopcart:
        total += product.product.price * product.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():

            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.country = form.cleaned_data['country']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            ordercode = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=7))
            data.code = ordercode
            data.save()

            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for product in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = product.product_id
                detail.user_id = current_user.id
                detail.quantity = product.quantity
                detail.price = product.product.price
                detail.amount = product.amount
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, 'Your Order has been completed. Thank you.')
            return render(request, 'Order_Completed.html', {'ordercode': ordercode, 'category': category})
        else:
            messages.warning(request, form.errors)
            return redirect('/order/orderproduct')

    form = OrderForm()
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    profile = Profile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'Order_Form.html', context)
