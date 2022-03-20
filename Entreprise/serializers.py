from rest_framework import serializers

from Entreprise.models import Entreprise

class EntrepriseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entreprise
        fields = '__all__'
        #fields = ('id', 'nomEntreprise')
