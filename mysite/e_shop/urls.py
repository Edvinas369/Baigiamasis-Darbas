from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
<<<<<<< HEAD
=======
    path('login/', views.login, name='login'),
>>>>>>> b4afd4b4b704e09f571a00eada66fb1cba28c5d0
]