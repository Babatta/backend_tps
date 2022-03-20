from django.urls import path
from . import views

urlpatterns = [
    path('list-demande', views.demande),

]