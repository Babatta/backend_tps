from django.db import models

from SousSecteur.models import SousSecteur
# Create your models here.

class Entreprise(models.Model):
    nomEntreprise = models.CharField(max_length=100,null=True)
    ninea = models.CharField(max_length=100,null=True)
    formeJuridique = models.CharField(max_length=100,null=True)
    adresse = models.CharField(max_length=100,null=True)
    telephone = models.IntegerField(null=True)
    siteInternet = models.URLField(max_length=100,null=True)
    email =  models.EmailField(null=True)
    capitalSocial = models.FloatField(null=True)
    chiffreAffaire = models.FloatField(null=True)
    effectif = models.IntegerField(null=True)
    directeurGeneral = models.CharField(max_length=100,null=True)
    activite= models.CharField(max_length=255,null=True)
    souSecteur = models.ManyToManyField(SousSecteur)

    def __str__(self):
        return self.nomEntreprise

# class Contenir(models.Model):,through='Contenir'
#     entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)
#     sousecteur = models.ForeignKey(SousSecteur,on_delete=models.CASCADE)