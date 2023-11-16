from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Item

# Create your views here.


def login(request):
    
    return render(request,'./authentication/login.html',)

def index(request):
    
    return render(request,'index.html',)