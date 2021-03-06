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
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


from food.models import Favorite, Product

# Create your views here


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None


def user_login(request):
    if request.method == 'GET':
        return render(request, 'usermanagement/login.html', {'form': LoginForm})
    else:
        print('request POST', request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)
        print('user =', user)
        user_authentication = authenticate(
            username=user, password=password)
        if user_authentication is None:
            return render(request, 'usermanagement/login.html', {'form': LoginForm(), 'error': 'email and password do not match or the email does not exist'})
        else:
            login(request, user)
            return redirect('home')


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'usermanagement/signup.html', {'form': UserCreateForm})
    else:
        details = UserCreateForm(request.POST)
        if details.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = request.POST['email']
                user.username = request.POST['username']
                user.save()
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'usermanagement/signup.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})
        else:
            form = UserCreateForm(None)
            print('errooor', details.errors)
            return render(request, 'usermanagement/signup.html', {'form': form, 'errors': details.errors})


def logout_user(request):
    logout(request)
    return redirect('home')


def account_user(request):
    return render(request, 'usermanagement/account.html')


def add_to_favorite(request, product_id):
    user = request.user
    #print('user id ===', request.user.id)
    product = get_object_or_404(Product, pk=product_id)
    #print('get object', get_object_or_404(Favorite, pk=product_id))

    #test_if_here = get_object_or_404(Favorite, pk=product_id)
    try:
        fav_obj_product = Favorite.objects.all()
    except Favorite.DoesNotExist:
        raise Http404("No model matches the given query")

    #print('-------------------', vars(fav_obj_product[0]))

    for x in fav_obj_product:
        #print('user is', x.user_id)
        #print('the favorite object is', x.product_id)

        if(x.user_id == request.user.id and x.product_id == product_id):
            return render(request, 'usermanagement/already_in_favorite.html')
    #print('current user ===', user)
    #print('see the product', fav_obj_product)
    #print('see the user', fav_obj_product.user)
    favorite = Favorite.objects.create(user=user, product=product,
                                       favorite_object_id=product_id)
    favorite.save()
    return render(request, 'usermanagement/add_to_favorite.html', {'user': user, 'product': product})


def display_favorites(request):
    if request.user.is_authenticated:
        current_user = request.user
        favorite = Favorite.objects.filter(user=current_user)
        print('my favvv', favorite)
        #print('my favvv 1', favorite[0].product.nutriscore_letter)
        return render(request, 'usermanagement/my_favorites.html', {'favorite': favorite})

    else:
        return redirect('home')
