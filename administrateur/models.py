from django.db import models

# Create your models here.
from utilisateur.models import utilisateur


class administrateur(models.Model):
    utilisateur = models.ForeignKey(utilisateur, null=True, on_delete=models.SET_NULL)


