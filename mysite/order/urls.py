from django.urls import include, path

from . import views

urlpatterns = [
    path('order/', views.order, name='order'),

]
