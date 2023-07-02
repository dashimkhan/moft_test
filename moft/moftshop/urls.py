from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('<slug:category_slug>/', product_list),
]