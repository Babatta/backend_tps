from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.


def utilisateur(request):
    return HttpResponse('Bienvenue utilisateur')