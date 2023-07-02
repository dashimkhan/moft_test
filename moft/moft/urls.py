from django.contrib import admin
from django.urls import path, include
from moftshop.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('moftshop.urls')),
]
