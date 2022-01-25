from cgi import test
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserCreateForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


from food.models import Favorite, Product

# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'usermanagement/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('home')


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'usermanagement/signup.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'usermanagement/signup.html', {'form': UserCreationForm, 'error': 'Passwords do not match'})


def logout_user(request):
    logout(request)
    return redirect('home')


def account_user(request):
    return render(request, 'usermanagement/account.html')


def add_to_favorite(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    print('get object', get_object_or_404(Favorite, pk=product_id))

    test_if_here = get_object_or_404(Favorite, pk=product_id)
    if test_if_here:
        return render(request, 'usermanagement/already_in_favorite.html')
    favorite = Favorite.objects.create(user=user, product=product,
                                       favorite_object_id=product_id)
    favorite.save()
    return render(request, 'usermanagement/add_to_favorite.html', {'user': user, 'product': product})


def display_favorites(request):
    current_user = request.user
    favorite = Favorite.objects.filter(user=current_user)
    print('my favvv', favorite)
    print('my favvv 1', favorite[0].product.nutriscore_letter)
    return render(request, 'usermanagement/my_favorites.html', {'favorite': favorite})
