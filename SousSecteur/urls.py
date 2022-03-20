from django.urls import path
from rest_framework import routers
from SousSecteur import views
from SousSecteur.views import SouSecteurViewSet


urlpatterns = [
    path('/SouSecteur',views.api_sousecteur),
    path('/list-sousecteur', views.list_sousecteur),

]


routerSousSecteur = routers.DefaultRouter()
routerSousSecteur.register('',SouSecteurViewSet)