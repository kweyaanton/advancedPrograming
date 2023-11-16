from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request): 
    
    return render(request,'index.html',)


def home(request):
    words = request.POST['text']
    numberOfw = len(words.split())
    return render(request,'home.html',{'number':numberOfw})