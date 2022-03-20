from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from SousSecteur.models import SousSecteur
from SousSecteur.serializers import SousSecteurSerializer


@api_view(['GET'])
def api_sousecteur(request):
    api_urls = {
        'List':'list-sousecteur',
}
    return Response(api_urls)

@api_view(['GET'])
def list_sousecteur(request):
    list = SousSecteur.objects.all().select_related('secteur')
    for sec in list:
        print(sec.nomSousSecteur,sec.secteur.nomSecteur)
    serializer = SousSecteurSerializer(list,many=True)
    return Response(serializer.data)

class SouSecteurViewSet(viewsets.ModelViewSet):

    queryset = SousSecteur.objects.all()
    serializer_class = SousSecteurSerializer