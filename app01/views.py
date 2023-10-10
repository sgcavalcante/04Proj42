from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 

from app01.models import Dados
from app01.forms import DadosForm

# Create your views here.


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


def remover(request,id):
    dado = get_object_or_404(Dados,pk=id)
    dado.delete()
    return redirect('listar_dados')


#fields = ['nome','telefone','email','cidade','subestacao','nivel_tensao_AT','nivel_tensao_BT']
def editar(request,id):
    dado = get_object_or_404(Dados,pk=id)
    if request.method =='GET':
        form = DadosForm(initial={'nome':dado.nome,'telefone':dado.telefone,'email':dado.email,'cidade':dado.cidade,'subestacao':dado.subestacao,'nivel_tensao_AT':dado.nivel_tensao_AT,'nivel_tensao_BT':dado.nivel_tensao_BT})
    elif request.method =='POST':
        form = DadosForm(request.POST)
        if form.is_valid():
            dado.nome = form.cleaned_data['nome']
            dado.telefone = form.cleaned_data['telefone']
            dado.email = form.cleaned_data['email']
            dado.cidade = form.cleaned_data['cidade']
            dado.subestacao = form.cleaned_data['subestacao']
            dado.nivel_tensao_AT = form.cleaned_data['nivel_tensao_AT']
            dado.nivel_tensao_BT = form.cleaned_data['nivel_tensao_BT']
            dado.save()
            return redirect('listar_dados')
                
    return render (request,'Editar_Dados.html',{"form":form,"id":id})