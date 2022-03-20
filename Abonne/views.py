from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listabonne(request):
    return HttpResponse('Bienvenue Administrateur')