from django.urls import path
from . import views


urlpatterns = [
    path('list_administateur', views.administrateur),
]