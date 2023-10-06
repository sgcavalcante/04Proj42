from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html') #index.html

#def area_restrita(request):
    #return render(request,'area_restrita')

