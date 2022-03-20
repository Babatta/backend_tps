from rest_framework import serializers

from Secteur.models import Secteur

class SecteurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secteur
        fields = '__all__'