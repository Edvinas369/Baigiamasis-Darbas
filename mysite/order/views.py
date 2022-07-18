from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Category
from order.models import ShopCart
from django.contrib import messages

def order(request):
    return render(request, 'order.html')



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

