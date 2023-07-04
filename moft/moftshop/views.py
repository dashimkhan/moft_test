from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductType
from django.http import HttpResponse



menu = ['Для телефона', 'Для планшета', 'Для ноутбука']

def about(request):
    return render(request, 'moftshop/about.html', {'title': 'О сайте'})

def contact(request):
    return render(request, 'moftshop/contact.html', {'title': 'Контакты'})

def index(request):
    typeHolder = ProductType.objects.get(code='holder')
    phonesCategory = Category.objects.get(code='phone')
    tabletCategory = Category.objects.get(code='tablet')
    laptopCategory = Category.objects.get(code='laptop')

    phoneHolders = Product.objects.filter(productType=typeHolder.id, category=phonesCategory.id).all()
    tabletHolders = Product.objects.filter(productType=typeHolder.id, category=tabletCategory.id)
    laptopHolders = Product.objects.filter(productType=typeHolder.id, category=laptopCategory.id)

    return render(request, 'moftshop/index.html',
                  {
                      'title': 'Главная страница',
                      'phoneHolders': phoneHolders,
                      'tabletHolders': tabletHolders,
                      'laptopHolders': laptopHolders
                  })

def shopping_cart(request):
    return render(request, 'moftshop/shopping-cart.html', {'title': 'Корзина'})

# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'shop/product/detail.html', {'product': product})


