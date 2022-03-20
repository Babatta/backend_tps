from django.db import models
from utilisateur.models import utilisateur
# Create your models here.
import Abonne


class Abonne(models.Model):
    utilisateur = models.ForeignKey(utilisateur, null=True, on_delete=models.SET_NULL)

def __str__(self):
        return self.utilisateur