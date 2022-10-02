from django.urls import path
from . import views

urlpatterns = [
    path("accueil/", views.accuiel_contributeur, name="accueil_user_url"),
    path("traitement/", views.traitement_contributeur, name='traitement_user_url'),
    path("execution/<str:pk>/", views.execution_contributeur, name='execution_user_url'),
    path("affichage/", views.affiche_contributeur, name="affiche_journal"),
    path("executionModif/", views.execution_modif, name="execution_modif")
]