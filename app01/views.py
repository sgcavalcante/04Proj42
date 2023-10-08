from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

from app01.models import Dados
from .forms import DadosForm

# Create your views here.
def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def area_restrita(request):
    return render(request,'area_restrita.html')
 
def cadastrar_dados(request):
    if request.method=='POST':
        form = DadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dados')
    else:
        form = DadosForm()
    return render(request,'Cadastrar_Dados.html',{'form':form})

def listar_dados(request):
    dados1 = Dados.objects.all()
    return render(request,'listar_dados.html',{'Dados':dados1})