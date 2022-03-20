from rest_framework import serializers

from Abonne.models import Abonne

class AbonneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abonne
        fields = '__all__'