from django.urls import path
from . import views

urlpatterns = [
    path('list-utilisateur', views.utilisateur),

]