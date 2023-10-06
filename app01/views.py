from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(requisicao):
    return render(requisicao,'index.html') #index.html
