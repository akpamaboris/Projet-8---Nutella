from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from food.models import Product

# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchProduct')
    print(searchTerm)
    return render(request, 'pages/home.html', {})


def searchForProduct(request):
    searchTerm = request.GET.get('searchProduct')
    products = Product.objects.filter(name_of_product__icontains=searchTerm)
    print(products)
    return render(request, 'pages/test.html', {'products': products, 'searchTerm': searchTerm})
