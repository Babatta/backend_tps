from django.db import models

class utilisateur(models.Model):
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    adresse =  models.CharField(max_length=100,null=True)
    telephone = models.IntegerField(null=True)
    email =  models.EmailField(null=True)
    login = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    Mode = (('orangemoney', 'Orange Money'),
            ('wave', 'Wave'),
            ('virement', 'Virement Bancaire'))
    modepaiement = models.CharField(max_length=100, null=True, choices=Mode)

    def __str__(self):
        return self.prenom

#
# def utilisateur():
#     return None