"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Entreprise.urls import routerEntreprise as entreprise_routeur
from Secteur.urls import routerSecteur as secteur_routeur
from SousSecteur.urls import routerSousSecteur as soussecteur_routeur

routerEntreprise = routers.DefaultRouter()
routerEntreprise.registry.extend(entreprise_routeur.registry)

routerEntreprise.registry.extend(secteur_routeur.registry)
routerEntreprise.registry.extend(soussecteur_routeur.registry)

routerSecteur = routers.DefaultRouter()
routerSecteur.registry.extend(secteur_routeur.registry)

routerSousSecteur = routers.DefaultRouter()
routerSousSecteur.registry.extend(soussecteur_routeur.registry)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('Entreprise.urls')),
     path('entreprise', include(routerEntreprise.urls)),
     path('secteur', include(routerSecteur.urls)),
     path('secteurs', include('Secteur.urls')),
     path('soussecteur', include(routerSousSecteur .urls)),
     path('soussecteurs', include('SousSecteur.urls')),
     path('administrateur', include('administrateur.urls')),
     path('utilisateur', include('utilisateur.urls')),
     path('abonne', include('Abonne.urls')),
     path('demande', include('DemandeAbonnement.urls')),
]