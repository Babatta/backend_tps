from rest_framework import routers
from Entreprise.views import EntrepriseViewSet
from Entreprise.views import list_entreprise
from Entreprise.views import apiOverview

from django.urls import path
from . import views

urlpatterns = [
    path('api-overview',views.apiOverview),
    path('list-entreprise', views.list_entreprise),

]

routerEntreprise = routers.DefaultRouter()
routerEntreprise.register('',EntrepriseViewSet)

