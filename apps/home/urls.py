# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # -- ADMIN USER -- #
        #++Journal page
    path('Journal/', views.journal, name="jrnl"),
    
        #++Contributeur page
    path('Contributeur/', views.contributeur, name="contrib"),
    
        #++Recapitulation page
    path('Recapitulation/' , views.recapitulation, name="recap"),
    
    
    # -- SIMPLE USER -- #
        #++Accueil
    path('User/', views.utilisateur , name="accueil_user_url"),
        #++Traitement
    path('Traitement/', views.traitement_user , name='traitement_user_url'),
        #++Execution
    path('Execution_du_journal/', views.execution_user , name='execution_user_url'),
        #++Affichage journal
    path('Affichage/', views.affichage_user, name="affiche_journal"),
        #++Rapport_user
    path('Mon_rapport/', views.rapport_user, name='rapp_user'),
    
    # The home page
    path('Accueil/', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
