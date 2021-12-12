from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    return render(request, 'pages/home.html', {})
