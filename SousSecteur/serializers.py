from rest_framework import serializers

from SousSecteur.models import SousSecteur

class SousSecteurSerializer(serializers.ModelSerializer):

    class Meta:
        model = SousSecteur
        fields = '__all__'