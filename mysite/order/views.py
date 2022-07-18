from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product, Category
from order.models import ShopCart, ShopCartForm
from django.contrib import messages


def order(request):
    return render(request, 'order.html')


@login_required
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = Product.objects.get(pk=id)

    if product.variant != 'None':
        variantid = request.POST.get('variantid')
        checkinvariant = ShopCart.objects.filter(
            variant_id=variantid, user_id=current_user.id)
        if checkinvariant:
            control = 1
        else:
            control = 0
    else:
        checkinproduct = ShopCart.objects.filter(
            product_id=id, user_id=current_user.id)
        if checkinproduct:
            control = 1
        else:
            control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                if product.variant == 'None':
                    data = ShopCart.objects.get(
                        product_id=id, user_id=current_user.id)
                else:
                    data = ShopCart.objects.get(
                        product_id=id, variant_id=variantid, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.variant_id = variantid
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")

    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.variant_id = None
            data.save()
        messages.success(request, "Product added to Shopcart")


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
    messages.success(request, "Your item deleted form Shopcart.")
    return redirect('/shopcart')
