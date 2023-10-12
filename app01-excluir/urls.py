from django.urls import path
from apps.app01.views import index,area_restrita,cadastrar_dados,listar_dados,remover,editar
urlpatterns = [
                
                path('index',index,name='index'),
                path('area_restrita/',area_restrita,name='area_restrita'),
                path('cadastrar_dados/',cadastrar_dados,name='cadastrar_dados'),
                path('listar_dados/',listar_dados,name='listar_dados'),
                path('remover/<int:id>',remover,name='remover'),
                path('editar/<int:id>',editar,name='editar')
]