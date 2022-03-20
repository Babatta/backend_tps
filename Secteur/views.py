from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Secteur.models import Secteur
from Secteur.serializers import SecteurSerializer

@api_view(['GET'])
def api_secteur(request):
    api_urls = {
        'list-secteur':'list-secteur',
}
    return Response(api_urls)

@api_view(['GET'])
def list_secteur(request):
    list = Secteur.objects.all().order_by('-id')
    serializer = SecteurSerializer(list,many=True)
    return Response(serializer.data)

class SecteurViewSet(viewsets.ModelViewSet):

    queryset = Secteur.objects.all()
    serializer_class = SecteurSerializer

