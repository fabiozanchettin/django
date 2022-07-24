from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def funcLogin(request):
    return render(request, 'login.html' )

def pagHome(request):
    return render(request, 'home.html', context={
        'nome': 'fabio',
        'salario':100000
    })