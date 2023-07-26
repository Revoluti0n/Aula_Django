from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    #return HttpResponse('Bem vindo à página do Django (Welcome to the DJANGO).')
    return render(request, 'index.html', {})