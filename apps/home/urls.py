# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # -- ADMIN USER -- #
    path('journal/', views.journal, name="jrnl"),
    path('contributeur/', views.contributeur, name="contrib"),
    path('action/', views.action, name="action"),
    path('statutJournal/', views.statut_journal),
    path('statutTache/', views.statut_tache),
    path('recapitulation/' , views.recapitulation, name="recap"),
    path('profile/', views.profil_info, name="profile"),
    

    path('contributeur/monRapport/', views.rapport_user, name='rapp_user'),
    
    # The home page
    path('Accueil/', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
