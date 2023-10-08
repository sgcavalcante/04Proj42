from django.urls import path
from app01.views import index,area_restrita,cadastrar_dados,listar_dados,login
urlpatterns = [
                path('',login,name='index'),
                path('index',index,name='index'),
                path('area_restrita/',area_restrita,name='area_restrita'),
                path('cadastrar_dados/',cadastrar_dados,name='cadastrar_dados'),
                path('listar_dados/',listar_dados,name='listar_dados')
]