from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.

def demande(request):
    return HttpResponse('Bienvenue Demande abonnement')