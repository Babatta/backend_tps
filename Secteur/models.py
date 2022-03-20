from django.db import models
# from Entreprise.models import Entreprise
# from SousSecteur.models import SousSecteur


class Secteur(models.Model):
    SECTEUR = (('Commerce','Commerce'),
                  ('Industrie','Industrie'),
                  ('Service','Service'))
    nomSecteur = models.CharField(max_length=100,null=True,choices=SECTEUR)
    # soussecteur = models.ForeignKey(SousSecteur,null=True,on_delete=models.SET_NULL)
    # entreprise = models.ForeignKey(Entreprise,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.nomSecteur