from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.


def user_login(request):
    return render(request, 'usermanagement/login.html', {'form': LoginForm})


def signup(request):
    if request.method == 'GET':
        return render(request, 'usermanagement/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
