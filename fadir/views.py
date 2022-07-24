from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def funcLogin(request):
    return render(request, 'pages/login.html' )

def pagHome(request):
    return render(request, 'pages/home.html', context={
        'nome': 'FADIR',
        'salario':100000
    })