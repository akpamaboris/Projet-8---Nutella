from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from food.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchProduct')
    print(searchTerm)
    return render(request, 'pages/home.html', {})


def searchForProduct(request):
    searchTerm = request.GET.get('searchProduct')
    products = Product.objects.filter(name_of_product__icontains=searchTerm)
    print('the products', products)
    return render(request, 'pages/productsresearch.html', {'products': products, 'searchTerm': searchTerm})


def searchDetailProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/productdetail.html', {'product': product})


def contactPage(request):
    return render(request, 'pages/contact.html')


def legalMentions(request):
    return render(request, 'pages/legalmentions.html')
