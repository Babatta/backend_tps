from django.db import models

from Secteur.models import Secteur
# Create your models here.
class SousSecteur(models.Model):
    nomSousSecteur = models.CharField(max_length=100,null=True)
    secteur = models.ForeignKey(Secteur,null=True,on_delete=models.SET_NULL)
    # entreprise = models.ManyToManyField('Entreprise', through='Contenir')

    def __str__(self):
        return self.nomSousSecteur