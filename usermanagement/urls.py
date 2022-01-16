from django.contrib import admin, auth
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('signup', views.signup_user, name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('account', views.account_user, name="account_user"),
    path('add-to-favorite/<int:product_id>',
         views.add_to_favorite, name="add_to_favorite"),
    path('viewfavorites', views.display_favorites, name="viewfavorites")

]
