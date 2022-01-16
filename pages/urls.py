from django.contrib import admin, auth
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('search', views.searchForProduct, name='search'),
    path('<int:product_id>', views.searchDetailProduct, name='searchdetail'),

]
