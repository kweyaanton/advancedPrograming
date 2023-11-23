from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):

    return render(request,'./authentication/login.html',)

def signup(request):
    username = request.POST['username']
    password = request.POST['password']

    data = {
        'username':username,
        'password':password,
    }
    
    
    return render(request,'./authentication/signup.html',{'data':data})

def index(request):
    
    return render(request,'index.html',)

def checkout(request):
    
    return render(request,'checkout.html',)