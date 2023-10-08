from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from apps.appLogin.forms import LoginForm

from .forms import RegistrationForm

# Create your views here.

def login(request):
    formulario = LoginForm()
    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha'].value()
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )

        if usuario is not None:
            auth.login(request,usuario)
            return redirect('index')
        else:
            return redirect('login')
    
    return render(request,'Login/login.html',{'form':formulario})


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,email=email,password=password)
            user = authenticate(username=username,password=password)
            #login(request)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'Login/registro.html',{'form':form})