from django.urls import path
from .views import getResp,getUplPage,getTest,getAct

urlpatterns = [
    path('',getUplPage,name='docchecker'),
    path('getres',getResp, name='getres'),
    path('test',getTest,name='test'),
    path('tstres',getAct,name='tstres')
]