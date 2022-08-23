# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # -- ADMIN USER -- #
        #++Journal page
    path('journal/', views.journal, name="jrnl"),
    
        #++Contributeur page
    path('contributeur/', views.contributeur, name="contrib"),
    
        #++Recapitulation page
    path('recapitulation/' , views.recapitulation, name="recap"),
    
    

    path('contributeur/monRapport/', views.rapport_user, name='rapp_user'),
    
    # The home page
    path('Accueil/', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
