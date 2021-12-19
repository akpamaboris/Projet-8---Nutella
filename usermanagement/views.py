from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

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
        return render(request, 'usermanagement/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'usermanagement/signup.html', {'form': UserCreationForm, 'error': 'Passwords do not match'})


def logout_user(request):
    logout(request)
    return redirect('home')
