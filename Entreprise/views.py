from django.shortcuts import render
from rest_framework import viewsets
from Entreprise.models import Entreprise
from Secteur.models import Secteur
from SousSecteur.models import SousSecteur
from Entreprise.serializers import EntrepriseSerializer
from Secteur.serializers import SecteurSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'list-entreprise',
}
    return Response(api_urls)

@api_view(['GET'])
def list_entreprise(request):
    list = Entreprise.objects.all().order_by('-id')
    for li in list:
        print(li.nomEntreprise)
    serializer = EntrepriseSerializer(list,many=True)
    secteur = Secteur.objects.all().order_by('-id')
    context = {'secteurs': secteur}
    return Response(serializer.data)

class EntrepriseViewSet(viewsets.ModelViewSet,ListAPIView):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    # permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination
    filterset_fields = ['nomEntreprise','formeJuridique','chiffreAffaire','souSecteur']
    search_fields = ['adresse']

