from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('orders-history/', orders_history, name='orders-history'),
    path('order/', order, name='order'),
]