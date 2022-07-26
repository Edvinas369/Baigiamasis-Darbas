from django.urls import include, path

from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='orddeletefromcarter'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

]
