from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def funcLogin(request):
    return HttpResponse('informe seus dados')

def pagHome(request):
    return HttpResponse('Essa é a nova home - pesquise prova')