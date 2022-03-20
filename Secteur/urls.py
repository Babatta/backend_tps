from django.urls import path
from rest_framework import routers
from Secteur import views
from Secteur.views import SecteurViewSet

urlpatterns = [
    path('/apiSecteur',views.api_secteur),
    path('/list-secteur', views.list_secteur),

]


routerSecteur = routers.DefaultRouter()
routerSecteur.register('',SecteurViewSet)