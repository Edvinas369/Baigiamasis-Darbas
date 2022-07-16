from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contactus'),
    path('cart/', views.cart, name='cart'),
    path('refund/', views.refund, name='refund'),
    path('product_details/', views.product_details, name='product_details'),
]
