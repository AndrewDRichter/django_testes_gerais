from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo a Home")

def teste(request):
    return HttpResponse("<h1>Testando rotas</h1></ br><ul><li>Item 1</li></ul>")