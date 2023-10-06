from django.urls import path
from app01.views import index#,arearestrita,home,cadastrar_subestacao,listar_produtos
urlpatterns = [
    
    path('',index,name='index'),
     
]