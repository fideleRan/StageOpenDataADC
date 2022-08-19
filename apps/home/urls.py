# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # -- ADMIN USER -- #
        #++Journal page
    path('adminUser/journal/', views.journal, name="jrnl"),
    
        #++Contributeur page
    path('adminUser/contributeur/', views.contributeur, name="contrib"),
    
        #++Recapitulation page
    path('adminUser/recapitulation/' , views.recapitulation, name="recap"),
    
    
    # -- SIMPLE USER -- #
        #++Accueil
    # path('contributeur/user/', views.utilisateur , name="accueil_user_url"), # ovaina
    #     #++Traitement
    # path('contributeur/traitement/', views.traitement_user , name='traitement_user_url'),
    #     #++Execution
    # path('contributeur/executionDuJournal/', views.execution_user , name='execution_user_url'),
    #     #++Affichage journal
    # path('contributeur/affichage/', views.affichage_user, name="affiche_journal"),
        #++Rapport_user
    path('contributeur/monRapport/', views.rapport_user, name='rapp_user'),
    
    # The home page
    path('Accueil/', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
