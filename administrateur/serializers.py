from rest_framework import serializers

from administrateur.models import administrateur

class administrateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = administrateur
        fields = '__all__'